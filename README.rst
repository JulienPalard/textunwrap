==========
textunwrap
==========


.. image:: https://img.shields.io/pypi/v/textunwrap.svg
        :target: https://pypi.python.org/pypi/textunwrap

.. image:: https://img.shields.io/travis/JulienPalard/textunwrap.svg
        :target: https://travis-ci.org/JulienPalard/textunwrap

.. image:: https://readthedocs.org/projects/textunwrap/badge/?version=latest
        :target: https://textunwrap.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/julienpalard/textunwrap/shield.svg
     :target: https://pyup.io/repos/github/julienpalard/textunwrap/
     :alt: Updates


Tries to reverse ``textwrap.wrap()``.

* Documentation: https://textunwrap.readthedocs.io.


Usage
-----

The ``textunwrap`` package exposes a ``unwrap`` function, unwrapping a
given string like:

.. code-block:: pycon

    >>> from textwrap import fill
    >>> from textunwrap import unwrap
    >>> print(fill("foo " * 100))
    foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo
    foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo
    foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo
    foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo
    foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo
    foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo
    >>> print(unwrap(fill("foo " * 100)))
    foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo foo


Command line usage
------------------

A ``textunwrap`` (and a ``textwrap``) command line are provided:

.. code-block:: shell-session

    $ cat APAFML-wrapped.txt
    Copyright (c) 1985, 1987, 1989, 1990, 1991, 1992, 1993, 1997 Adobe Systems
    Incorporated. All Rights Reserved.

    This file and the 14 PostScript(R) AFM files it accompanies may be used,
    copied, and distributed for any purpose and without charge, with or without
    modification, provided that all copyright notices are retained; that the AFM
    files are not distributed without this file; that all modifications to this
    file or any of the AFM files are prominently noted in the modified file(s); and
    that this paragraph is not modified. Adobe Systems has no responsibility or
    obligation to support the use of the AFM files.

    $ textunwrap APAFML-wrapped.txt
    Copyright (c) 1985, 1987, 1989, 1990, 1991, 1992, 1993, 1997 Adobe Systems Incorporated. All Rights Reserved.

    This file and the 14 PostScript(R) AFM files it accompanies may be used, copied, and distributed for any purpose and without charge, with or without modification, provided that all copyright notices are retained; that the AFM files are not distributed without this file; that all modifications to this file or any of the AFM files are prominently noted in the modified file(s); and that this paragraph is not modified. Adobe Systems has no responsibility or obligation to support the use of the AFM files.


Contributing
------------

The algorithm used can by far be enhanced, to help with this or simply
to analyze the current behavior, a ``textwrap`` command line tool is
also provided, so you can take any file, wrap it to different widths,
unwrap it again and see what it gives back, like:

.. code-block:: shell-session

  $ diff tests/licenses/APAFML.txt <(cat tests/licenses/APAFML.txt | textwrap -w 70 - | textunwrap -)
  $ diff tests/licenses/APAFML.txt <(cat tests/licenses/APAFML.txt | textwrap -w 80 - | textunwrap -)


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
