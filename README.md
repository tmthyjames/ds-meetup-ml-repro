# reproml

This repo contains the `reproml` project.

## Development Pre-Requisites

To work with this repo install the following prerequisites:

* python 3.8+ - [anaconda](https://www.anaconda.com/distribution/) or [pyenv](https://github.com/pyenv/pyenv)
* pre-commit:

```
brew install pre-commit
```

* pipenv

```
conda install pip
pip install pipenv
```

**Setup for Development**

After prerequisites are installed, run the following commands to clone the repo and configure it for development:

```
cd <REPO_ROOT>

# Install pre-commit hooks to local clone
pre-commit install

# Install pipenv environment
pipenv install --dev

# Create IPython Kernel for the virtual environment
pipenv run ipython kernel install --user --name=reproml
```

The `pipenv install` command above creates an isolated virtual environment for this repo with
all dev dependencies installed. There are two main ways of using the virtual environment. To
run a one off command in the environment use `pipenv run`. For example, the following command
will show the location of the python executable for the environment:

```
pipenv run which python
```

Alternatively, for running many commands `pipenv shell` is used to spawn a new shell in the
virtual environment.

```
cd <REPO_ROOT>
pipenv shell
```

## Running Tests

To run the unit tests run the following command (optionally adding `--cov` for a coverage report):

```
pytest
```

## Troubleshooting

If you ever have trouble with the python environment,
many problems can be resolved by "rebooting" it
by running these commands in the repo root:

```
pipenv --rm
pipenv install --dev
```

This will resolve common problems with packages not being found, etc.



## Generating Documentation
* To update documentation, you can use `pipenv run docs`.
* You can then use `pipenv run open-docs` to see how your docs look in a browser.
```
cd <REPO ROOT>
pipenv run docs
pipenv run open-docs
```
