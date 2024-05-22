# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Project Organization

{% if cookiecutter.license != 'No license file' %}
    ├── LICENSE  
{% endif %}
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering)
    │                         and a short `-` delimited description, e.g. `1.0-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │
    ├── pyproject.toml     <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    |   ├── scripts        <- Scripts that not part of the module
    |   ├── {{ cookiecutter.repo_name }}    <- The module of this project, where you place custom preprocessors, data loader, model card plotter, model trainer and explainer, etc.
    │       ├── data                        <- classes to prepare, analyse or generate data
    │       ├── features                    <- classes to turn raw data into features for modeling
    │       ├── models                      <- train models and then use trained models to make
    │       └── visualization               <- create exploratory and results oriented visualizations

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

## Getting started

pip install poetry
poetry install


### Generate documentation

Theme documentation: https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html
apidoc documentation: https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html

#### Windows

```shell
cd docs
sphinx-apidoc -lfM -d 0 -o drg_analytic/ ../src/drg_analytic
.\make.bat html
```

#### Mac/Linux

```shell
cd docs
sphinx-apidoc -lfM -d 0 -o drg_analytic/ ../src/drg_analytic
make html
```


### Create package

```shell
python src/setup.py sdist
```


### Docker

#### Base imgae
docker build --target base -t {{cookiecutter.repo_name}}_base .  

#### Test
docker build --target test -t {{cookiecutter.repo_name}}_test .  