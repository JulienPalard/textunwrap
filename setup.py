#!/usr/bin/env python3

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()


setup(
    name='textunwrap',
    version='0.1.1',
    description="Tries to reverse textwrap.wrap.",
    long_description=readme,
    author="Julien Palard",
    author_email='julien@palard.fr',
    url='https://github.com/JulienPalard/textunwrap',
    packages=[
        'textunwrap',
    ],
    package_dir={'textunwrap':
                 'textunwrap'},
    entry_points={
        'console_scripts': [
            'textunwrap=textunwrap.textunwrap:run',
            'textwrap=textunwrap.textwrap:run'
        ]
    },
    include_package_data=True,
    install_requires=[],
    license="MIT",
    zip_safe=False,
    keywords='textunwrap',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=[]
)
