
# check-python-style github action

## Objecctive

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
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: VisiumCH/check-python-style@main
        with:
          python-version: "3.10"

```