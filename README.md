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
|   ├── {{ cookiecutter.repo_name }}    <- The module of this projectetc.
│       ├── data                        <- classes to prepare, analyse or generate data
│       ├── features                    <- classes to turn raw data into features for modeling
│       ├── models                      <- train models and then use trained models to make
│       └── visualization               <- create exploratory and results oriented visualizations

```
#### data
It is not a good practice to place alle your project data in this direcorty. Your data should only be stored in a data store in your organization environment. Use this directory only for testing purposes. That means, you can use this directory and all directories within to develop, test or debug your data processing.

#### docs
As above mentioned the docs directory is a Sphinx project. Use this project to creat a automated code documentation and to document you process, e.g, *Getting Startet*, *Data processing steps*, *Infrstrcuture*, ....

#### models
If your project is not mature enough and you don't have a centralized model registry use this directory to store models locally. Otherwise delete it.

#### notebooks
Notebooks are great for data discovery or to validate your hypothesis, but not for more. 

#### references

#### reporsts


#### src/{{ cookiecutter.repo_name }} 

Here you place custom preprocessors, data loader, model card plotter, model trainer and explainer, etc. You can see this as you core package of you project. This code has to be well engineered and tested so it can reliability used during data exploration in notebooks, traing and data pipelines or in model serving within a REST API.

#### src/scripts

In this directory you can place everything that glues your standardized code from src/{{ cookiecutter.repo_name }} together. Place your pipline code, frontends like Streamlit or your FastApi for model serving here.


### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests

