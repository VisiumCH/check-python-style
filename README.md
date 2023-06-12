[![Continuous Integration Pipeline](https://github.com/VisiumCH/check-python-style/actions/workflows/ci.yml/badge.svg)](https://github.com/VisiumCH/check-python-style/actions/workflows/ci.yml)

# check-python-style github action

## Objective

The purpose of this github action is to implement a CI that checks whether the code follows the Visium python guidelines.

## How to use it

You can add the following snippet of code in a file located in `.github/workflows`. Note that this is the CI that is used in `VisiumCH/cookiecutter`.

```yaml

name: Continuous Integration Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  check-python-style:
    uses: VisiumCH/.github/workflows/workflow.yml
    with:
      python-version: 3.11

```
