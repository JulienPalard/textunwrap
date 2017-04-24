#!/usr/bin/env python3

import textwrap
from textunwrap import __version__


def parse_args():
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    import argparse
    parser = argparse.ArgumentParser(
        description="Wrap a text file to a given width.")
    parser.add_argument(
        '--version',
        action='version',
        version='textwrap {ver}'.format(ver=__version__))
    parser.add_argument(
        dest="infile",
        type=argparse.FileType('r'),
        help="Input file path.",
        metavar="FILE")
    parser.add_argument(
        '--width', '-w',
        default=80,
        metavar=80,
        help="use width columns instead of 80.",
        type=int)
    return parser.parse_args()


def wrap_file(infile, width=80):
    """Wrap the given file to the given width.
    Returns the wrapped content as a string.
    """
    return '\n\n'.join(
        textwrap.fill(text, width) for text in
        infile.read().split('\n\n'))


def run():
    """Entry point for console_scripts
    """
    print(wrap_file(**vars(parse_args())))


if __name__ == "__main__":
    run()
