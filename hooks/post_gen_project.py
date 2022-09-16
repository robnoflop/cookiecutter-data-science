#!/usr/bin/env python
import os
import shutil
from typing import List
import yaml

MANIFEST = "manifest.yml"

SETTINGS = {
    'risk_management_report' : '{{ cookiecutter.risk_management_report }}',
    'experiment_blueprint' : '{{ cookiecutter.experiment_blueprint }}',
    'documentation_blueprint' : '{{ cookiecutter.documentation_blueprint }}'
}

def delete_resources_for_disabled_features():
    with open(MANIFEST) as manifest_file:
        manifest = yaml.safe_load(manifest_file)
    for k in manifest.keys():
        if SETTINGS[k] == 'False':
            delete_resource(manifest[k])
    print("cleanup complete, removing manifest...")
    delete_resource([MANIFEST])


def delete_resource(resources : List[str]):
    for resource in resources:
        if os.path.isfile(resource):
            print(f"removing file: {resource}")
            os.remove(resource)
        elif os.path.isdir(resource):
            print(f"removing directory: {resource}")
            shutil.rmtree(resource)


if __name__ == "__main__":
    delete_resources_for_disabled_features()

