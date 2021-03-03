#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_textunwrap
----------------------------------

Tests for `textunwrap` module.
"""

import os
import glob
import textwrap

import pytest

from textunwrap import textunwrap


FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'licenses/',
)


@pytest.mark.parametrize(
    "license_path",
    glob.glob(os.path.join(FIXTURE_DIR, '*.txt')))
def test_unwrap_licenses(license_path):
    with open(license_path) as license_file:
        license_text = license_file.read()
    for width in (70, 80, 85):
        wrapped = '\n\n'.join(
            textwrap.fill(text, width) for text in
            license_text.split('\n\n'))
        assert textunwrap.unwrap(wrapped) == license_text


def test_unwrap_custom_median_line_length():
    vsl_path = os.path.join(FIXTURE_DIR, 'VSL.md')
    with open(vsl_path) as license_file:
        license_text = license_file.read()
    single_line_text = license_text.replace('\n', ' ').strip()

    # check that unwrapping with default line length produces multi-line output
    default_unwrapped = textunwrap.unwrap(license_text).strip()
    assert default_unwrapped != single_line_text

    # check that unwrapping with custom line length produces single-line output
    custom_unwrapped = textunwrap.unwrap(license_text, median_len=15).strip()
    assert custom_unwrapped == single_line_text
