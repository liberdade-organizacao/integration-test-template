# Integration Tests Template

This is a template for integration tests using py.test and selenium.

## Setup

It's highly recommended that a virtual environment is setup for executing these
tests:

``` sh
python3 -m virtualenv venv -p python3
source venv/bin/activate  # or ./venv/Scripts/activate if you are on Windows
```

Ensure the required browser drives are installed in your machine.

- [For Firefox](https://github.com/mozilla/geckodriver/releases)
- [For Chrome](http://chromedriver.chromium.org/downloads)

Install the required packages to execute the tests:

```
pip install -r requirements.txt
```

Create an environment file. This can be done by copying the `.env.example` file:

``` sh
cp .env.example .env
nano .env  # to customize your environment as required
```

To execute all tests, execute:

```
pytest -vs --tb=line
```

## Development

### Environment variables

This project will try to load a file named `.env` to populate the environment
variables and configure your project.

There are a couple of variables that are used by default to configure the tests:

- `BROWSER`: set this `firefox` or `chrome` accordingly
- `HEADLESS`: set this value to anything if you want to run tests on a
  headless browser.

### Tests

This project uses [py.test](https://docs.pytest.org/en/latest/) as a base for
the unit test structure.

A couple of fixtures are already implemented for convinience, namely:

- `environment`: gives access to `os.environ` A.K.A. the environment variables
- `browser`: gives access to the Selenium webdriver as configured in the
  `.env` file

Sample tests are written on `tests/test_setup.py`.
