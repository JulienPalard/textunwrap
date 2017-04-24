.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:


Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/JulienPalard/textunwrap/issues.

If you are reporting a bug, please include detailed steps to reproduce
the bug, if possible the file used, or better a minimum sample file
reproducing the bug.


Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement it.


Enhance the algorithm
~~~~~~~~~~~~~~~~~~~~~

The current unwrapping algorithm is pretty dumb, any pull requests to
enhance it are welcome.


Get Started!
------------

Ready to contribute? Here's how to set up `textunwrap` for local development.

1. Fork the `textunwrap` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/textunwrap.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv textunwrap
    $ cd textunwrap/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox::

    $ flake8 textunwrap tests
    $ pytest

   To get flake8 and pytest, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add -p
    $ git commit -m "Your detailed description of your changes."
    $ git push -u origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.


Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.6, 2.7, 3.3, 3.4 and 3.5, and for PyPy. Check
   https://travis-ci.org/JulienPalard/textunwrap/pull_requests
   and make sure that the tests pass for all supported Python versions.
