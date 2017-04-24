#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_textunwrap
----------------------------------

Tests for `textunwrap` module.
"""

import os
import re
import glob
import textwrap

import pytest

from contextlib import contextmanager
from click.testing import CliRunner

from textunwrap import textunwrap
from textunwrap import cli


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
