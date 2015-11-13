# -*- coding: utf-8 -*-
import os
import re
from setuptools import setup, find_packages

here = lambda name: os.paht.join(os.path.abspath(os.path.dirname(__file__)), name)


def read(path, **kwargs):
    with open(path, 'rt') as fp:
        return fp.read()


def find_version(file_path):
    version_file = read(file_path)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


requires = [
    'six',
    ]

setup(
    name='taxlib.ja',
    version=find_version('src/taxlib/ja/__init__.py'),
    description='Tax library for japan',
    long_description=read('README.rst') + '\n\n' + read('CHANGES.rst'),
    classifiers=[
        'Development Status :: 1 - Planning',
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    author='TakesxiSximada',
    author_email='sximada@gmail.com',
    url='https://github.com/TakesxiSximada/taxlib.ja',
    keywords='Tax,Japan',
    packages=find_packages('src', exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={'': 'src'},
    namespace_packages=['taxlib'],
    include_package_data=True,
    zip_safe=False,
    test_suite='taxlib.ja',
    install_requires=requires,
    entry_points="""\
      [console_scripts]
      """,
    )
