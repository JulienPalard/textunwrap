=====
Usage
=====

To use textunwrap in a project, use the ``unwrap`` function exposed by
the ``textunwrap`` package:

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

Command line tools
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
