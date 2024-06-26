import os
import pytest
from subprocess import check_output
from conftest import system_check


def no_curlies(filepath):
    """ Utility to make sure no curly braces appear in a file.
        That is, was Jinja able to render everything?
    """
    with open(filepath, 'r') as f:
        data = f.read()

    template_strings = [
        '{{',
        '}}',
        '{%',
        '%}'
    ]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)


@pytest.mark.usefixtures("default_baked_project")
class TestCookieSetup(object):
    
    def test_project_name(self):
        project = self.path
        if pytest.param.get('project_name'):
            name = system_check('drivendata')
            assert project.name == name
        else:
            assert project.name == 'project_name'

    def test_author(self):
        pyproject_ = self.path / 'pyproject.toml'
        args = ['toml', 'get', '--toml-path', str(pyproject_), 'tool.poetry.authors']
        p = check_output(args).decode('ascii').strip()
        if pytest.param.get('author_name'):
            assert p == "['drivendata']"
        else:
            assert p == "['Your name (or your organization/company/team), format: name <email>']"

    def test_readme(self):
        readme_path = self.path / 'README.md'
        assert readme_path.exists()
        assert no_curlies(readme_path)
        if pytest.param.get('project_name'):
            with open(readme_path) as fin:
                assert 'drivendata' == next(fin).strip()

    def test_setup(self):
        pyproject_ = self.path / 'pyproject.toml'
        args = ['toml', 'get', '--toml-path', str(pyproject_), 'tool.poetry.version']
        p = check_output(args).decode('ascii').strip()
        assert p == '0.1.0'

    def test_license(self):
        license_path = self.path / 'LICENSE'
        assert license_path.exists()
        assert no_curlies(license_path)


    def test_folders(self):
        if pytest.param.get('project_name'):
            project_name = pytest.param.get('project_name').lower().replace(' ', '_')
        else:
            project_name = 'project_name'

        expected_dirs = [
            'data',
            'data/external',
            'data/interim',
            'data/processed',
            'data/raw',
            'docs',
            'models',
            'notebooks',
            'references',
            'reports',
            'reports/figures',
            'src',
            f'src/{project_name}',
            f'src/{project_name}/data',
            f'src/{project_name}/data/connectors',
            f'src/{project_name}/features',
            f'src/{project_name}/models',
            f'src/{project_name}/visualization',
            'src/scripts',
            'src/tests',
            'src/tests/test_data',
            'src/tests/test_data/1',
            'src/tests/test_data/2',
        ]

        ignored_dirs = [
            str(self.path)
        ]

        abs_expected_dirs = [str(self.path / d) for d in expected_dirs]
        abs_dirs, _, _ = list(zip(*os.walk(self.path)))
        print("abs_expected_dirs", abs_expected_dirs)
        print("ignored_dirs", len(ignored_dirs))
        print("abs_dirs", abs_dirs)
        print(set(abs_expected_dirs + ignored_dirs) - set(abs_dirs))
        assert len(set(abs_expected_dirs + ignored_dirs) - set(abs_dirs)) == 0

