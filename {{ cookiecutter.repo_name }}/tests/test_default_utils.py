import re
from {{ cookiecutter.repo_name }} import get_datetime_postfix
from {{ cookiecutter.repo_name }}.data import read_utils
from pathlib import Path


def get_test_data_path() -> Path:
    return Path(__file__).parent.resolve() / "test_data"
    

def test_get_datetime_postfix():
    postfix = get_datetime_postfix()
    assert re.match(r"\d{8}_\d{6}$", postfix) != None

def test_read_utils_get_all_files_in_path_all():
    file_list = read_utils.get_all_files_in_path(get_test_data_path())
    assert len(file_list) == 5

def test_read_utils_get_all_files_in_path_json_only():
    file_list = read_utils.get_all_files_in_path(get_test_data_path(), 'json')
    assert len(file_list) == 1

def test_read_utils_get_all_files_in_path_not_recursive():
    file_list = read_utils.get_all_files_in_path(get_test_data_path(), recursive=False)
    assert len(file_list) == 0
