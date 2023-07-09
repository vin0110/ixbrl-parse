# ixbrl-parse


![Test status](https://github.com/drkane/ixbrl-parse/workflows/tests/badge.svg)
[![PyPI version](https://img.shields.io/pypi/v/ixbrlparse)](https://pypi.org/project/ixbrlparse/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ixbrlparse)
![PyPI - License](https://img.shields.io/pypi/l/ixbrlparse)

A python module for getting useful data out of ixbrl files. The library is at an early stage - feedback and improvements are very welcome.

Full documentation is available at [dkane.net/ixbrl-parse/](https://dkane.net/ixbrl-parse/)

**[Changelog](https://dkane.net/ixbrl-parse/changelog/)**

## Requirements

The module requires [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [lxml](https://lxml.de/) to parse the documents.

[word2number](https://github.com/akshaynagpal/w2n) is used to process the
numeric items with the `numsenwords` format.

## How to install

You can install from pypi using pip:

```
pip install ixbrlparse
```

## How to use

You can run the module directly to extract data from an IXBRL file.

```bash
ixbrlparse example_file.html
# or
python -m ixbrlparse example_file.html
```

The various options for using this can be found through:

```bash
python -m ixbrlparse -h
# optional arguments:
#   -h, --help            show this help message and exit
#   --outfile OUTFILE     Where to output the file
#   --format {csv,json,jsonlines,jsonl}
#                         format of the output
#   --fields {numeric,nonnumeric,all}
#                         Which fields to output
```

You can also use as a python module (see [the documentation](https://dkane.net/ixbrl-parse/python-module/) for more details)

## Development

The module is setup for development using [hatch](https://hatch.pypa.io/latest/).

### Run tests

Tests can be run with `pytest`:

```bash
hatch run test
```

### Test coverage

Run tests then report on coverage

```bash
hatch run cov
```

Run tests then run a server showing where coverage is missing

```bash
hatch run cov-html
```

### Run typing checks

```bash
hatch run lint:typing
```

### Linting

Black and ruff should be run before committing any changes.

To check for any changes needed:

```bash
hatch run lint:style
```

To run any autoformatting possible:

```sh
hatch run lint:fmt
```

### Run all checks at once

```sh
hatch run lint:all
```

## Publish to pypi

```bash
hatch build
hatch publish
git tag v<VERSION_NUMBER>
git push origin v<VERSION_NUMBER>
```

## Acknowledgements

Originally developed for a project with 
[Power to Change](https://www.powertochange.org.uk/) looking at how to extract data from 
financial documents of community businesses.
