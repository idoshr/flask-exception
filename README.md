# Flask-Exception

[![PyPI version](https://badge.fury.io/py/flask-exception.svg)](https://badge.fury.io/py/flask-exception)
[![CI Tests](https://github.com/idoshr/flask-exception/actions/workflows/tests.yml/badge.svg)](https://github.com/flask/flask-exception/actions/workflows/tests.yml)
[![Documentation Status](https://readthedocs.org/projects/flask-exception/badge/?version=latest)](https://flask-exception.readthedocs.io/en/latest/?badge=latest)
[![Maintainability](https://api.codeclimate.com/v1/badges/6fb8ae00b1008f5f1b20/maintainability)](https://codeclimate.com/github/idoshr/flask-exception/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6fb8ae00b1008f5f1b20/test_coverage)](https://codeclimate.com/github/idoshr/flask-exception/test_coverage)
![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-exception)

Flask-Exception is a Flask extension that provides exception handling and logging for Flask applications.

## Installation

```bash
# For Flask >= 2.0.0
pip install flask-exception
```

## Flask configuration

Flask-exception does not provide any configuration defaults. User is responsible
for setting up correct database settings, to exclude any possible misconfiguration
and data corruption.

There are several options to set connection. Please note, that all except
recommended are deprecated and may be removed in future versions, to lower code base
complexity and bugs. If you use any deprecated connection settings approach, you should
update your application configuration.

Please refer to [complete connection settings description] for more info.

## Usage and API documentation

Full project documentation available on [read the docs].

## Contributing and testing

We are welcome for contributors and testers! Check [Contribution guidelines].

## License

Flask-Exception is distributed under [BSD 3-Clause License].
