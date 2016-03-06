![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)
![License](https://img.shields.io/badge/license-MIT%20License-blue.svg)

# xrff2csv

A Python tool that converts XRFF files to CSV format.

## License

Please see the [repository license](https://github.com/rhiever/xrff2csv/blob/master/LICENSE) for the licensing and usage information for xrff2csv.

Generally, we have licensed xrff2csv to make it as widely usable as possible.

## Installation

```bash
pip install xrff2csv
```

## Usage

xrff2csv can be used on the command line. Use `--help` to see its usage instructions.

```bash
xrff2csv --help

usage: xrff2csv [-h] [-o OUTPUT_FILENAME] [-sep SEP]
                [--ignore-update-check] [--version]
                INPUT_FILENAME

A Python tool that converts XRFF files to CSV format

positional arguments:
  INPUT_FILENAME        XRFF file to convert

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FILENAME    CSV file to output to
  -sep SEP              Separator in the CSV file (default: \t)
  --ignore-update-check
                        Do not check for the latest version of xrff2csv
                        (default: False)
  --version             show program's version number and exit
```

An example use on the command line would be:

```bash
xrff2csv zoo.xrff -o zoo.csv -sep ,
```

This command would convert `zoo.xrff` to `zoo.csv` with commas (,) as the separator.

xrff can also be used programmatically. An example use in code would be:

```python
from xrff2csv import xrff2csv

xrff2csv('zoo.xrff', 'zoo.csv', sep=',')
```

## Contributing to xrff2csv

We welcome you to [check the existing issues](https://github.com/rhiever/xrff2csv/issues/) for bugs or enhancements to work on. If you have an idea for an extension to xrff2csv, please [file a new issue](https://github.com/rhiever/xrff2csv/issues/new) so we can discuss it.
