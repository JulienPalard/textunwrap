# -*- coding: utf-8 -*-

import sys
from textunwrap import __version__
from textunwrap.textunwrap import unwrap


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    import argparse
    parser = argparse.ArgumentParser(
        description="Unwrap a wrapped text file.")
    parser.add_argument(
        '--version',
        action='version',
        version='textunwrap {ver}'.format(ver=__version__))
    parser.add_argument(
        '--wrap',
        help="Wrap instead of unwrapping, using std Python textwrap.")
    parser.add_argument(
        dest="file_path",
        help="Path to a file",
        metavar="FILE")
    return parser.parse_args(args)


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    if args.wrap:
        import textwrap
        with open(args.file_path) as file_to_wrap:
            text_to_wrap = file_to_wrap.read()
            wrapped = '\n\n'.join(
                textwrap.fill(text, 70) for text in
                text_to_wrap.split('\n\n'))
            print(wrapped)
    else:
        with open(args.file_path) as file_to_unwrap:
            print(unwrap(file_to_unwrap.read()), end="")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
