#!/usr/bin/env python3

"""Try to reverse textwrap.wrap.
"""

import re
from textunwrap import __version__


SPACES = r'(?:[ \t\f\v\u00A0\u2028])'
UNORDERED_LIST = r'(?:[*\u2022+])'
ORDERED_LIST = r'(?:[0-9]\.)'
BULLET_MARKER = r'(?:{unordered}|{ordered})'.format(
    ordered=ORDERED_LIST,
    unordered=UNORDERED_LIST)
BULLET_ITEM = r'(?:{spaces}*{bullet_marker}{spaces}+)'.format(
    bullet_marker=BULLET_MARKER,
    spaces=SPACES)


def unwrap(text, median_len=70):
    """Given a text composed of wrapped paragraphs, try to unwrap them.
    """
    in_bullet_list = False

    def from_same_paragraph(line_a, line_b, median_len=70):
        """Tries to determine if line_a and line_b are from the same
        paragraph.
        """
        nonlocal in_bullet_list
        if re.match(BULLET_ITEM, line_b):
            in_bullet_list = True
            return False
        if line_b.startswith(' ') and in_bullet_list:
            return True
        if not line_b and in_bullet_list:
            in_bullet_list = False
        if not line_a.strip():
            return False
        if ((median_len * .72 < len(line_a) < median_len * 2.5 and
             3 < len(line_b) < median_len * 2.5)):
            return True
        return False

    lines = text.split('\n')
    paragraphs = [[]]
    previous_line = ''
    for line in lines:
        if from_same_paragraph(previous_line, line, median_len):
            paragraphs[-1].append(line)
        elif line:
            paragraphs.append([line])
        previous_line = line
    return '\n\n'.join(' '.join(lines) for lines in paragraphs if lines) + '\n'


def parse_args():
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
        dest="infile",
        type=argparse.FileType('r'),
        help="Input file path.",
        metavar="FILE")
    return parser.parse_args()


def textunwrap_file(infile):
    """Unwrap a given opened file, returns the unwrapped content as a string.
    """
    return unwrap(infile.read())


def run():
    """Entry point for console_scripts
    """
    print(textunwrap_file(**vars(parse_args())), end="")


if __name__ == "__main__":
    run()
