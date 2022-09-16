# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


### Requirements to use the cookiecutter template:
-----------
 - Python 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

### To start a new project, run:
------------

    cookiecutter https://github.com/robnoflop/cookiecutter-data-science

### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
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
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
|   ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
|   ├── scripts        <- Scripts that not part of the module
|   ├── {{ cookiecutter.repo_name }}    <- The module of this project 
│       ├── data                        <- Scripts or classes to prepare, analyse or generate data
│       ├── features                    <- Scripts or classes to turn raw data into features for modeling
│       ├── models                      <- Scripts to train models and then use trained models to make
│       └── visualization               <- Scripts to create exploratory and results oriented visualizations
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```


### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests

