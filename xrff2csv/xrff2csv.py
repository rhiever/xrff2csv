# -*- coding: utf-8 -*-

"""
Copyright (c) 2016 Randal S. Olson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from __future__ import print_function
import os
import sys
import argparse
from update_checker import update_check

from ._version import __version__

update_checked = False

def xrff2csv(input_filename, output_filename=None, sep='\t', ignore_update_check=False):
    """Converts the provided XRFF file to CSV format

    If `output_filename` is not specified, the function will print the result

    Parameters
    ----------
    input_filename: str
        Name of the XRFF file to convert
    output_filename: str
        Name of the CSV file to output to (default: None)
    sep: str
        String to use as the separator in the CSV file (default: \t)
    ignore_update_check: bool
        Do not check for the latest version of xrff2csv

    Returns
    ----------
    None

    """
    global update_checked
    if ignore_update_check:
        update_checked = True

    if not update_checked:
        update_check('xrff2csv', __version__)
        update_checked = True
    with open(input_filename, 'r') as in_file:
        headers = []
        values = []
        for line in in_file:
            if 'attribute name=' in line:
                headers.append(line.split('"')[1])
            elif '<body>' in line:
                # Beginning of data entries has been encountered, so output the headers
                headers = sep.join(headers)
                if output_filename is not None:
                    with open(output_filename, 'w') as out_file:
                        out_file.write(headers)
                else:
                    sys.stdout.write(headers)
                # No need to store the headers in memory any more
                del headers
            elif '<value>' in line:
                values.append(line.split('>')[1].split('<')[0])
            elif '</instance>' in line:
                # End of data instance reached, so output it
                values = os.linesep + sep.join(values)
                if output_filename is not None:
                    with open(output_filename, 'a') as out_file:
                        out_file.write(values)
                else:
                    sys.stdout.write(values)
                # No need to store this data instance in memory any more
                values = []

    if output_filename is not None:
        with open(output_filename, 'a') as out_file:
            out_file.write(os.linesep)
    else:
        sys.stdout.write(os.linesep)

def main():
    """Main function that is called when xrff2csv is run on the command line"""
    parser = argparse.ArgumentParser(description='A Python tool that converts XRFF files to CSV format')

    parser.add_argument('INPUT_FILENAME', type=str, help='XRFF file to convert')

    parser.add_argument('-o', action='store', dest='OUTPUT_FILENAME', default=None,
                        type=str, help='CSV file to output to')

    parser.add_argument('-sep', action='store', dest='SEP', default='\t',
                        type=str, help='Separator in the CSV file (default: \\t)')

    parser.add_argument('--ignore-update-check', action='store_true', dest='IGNORE_UPDATE_CHECK', default=False,
                        help='Do not check for the latest version of xrff2csv (default: False)')

    parser.add_argument('--version', action='version',
                        version='xrff2csv v{version}'.format(version=__version__))

    args = parser.parse_args()

    xrff2csv(input_filename=args.INPUT_FILENAME, output_filename=args.OUTPUT_FILENAME,
             sep=args.SEP, ignore_update_check=args.IGNORE_UPDATE_CHECK)

if __name__ == '__main__':
    main()
