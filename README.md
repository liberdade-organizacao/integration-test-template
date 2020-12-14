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
