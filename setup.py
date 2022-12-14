#!/usr/bin/env python

from setuptools import setup
import re
import os
import sys


with open('README.md') as f:
    long_description = f.read()


def get_version(package):
    """Return package version as listed in `__version__` in `init.py`."""
    with open(os.path.join(package, '__init__.py')) as f:
        init_py = f.read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_packages(package):
    """Return root package and all sub-packages."""
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


setup(
    name="mkdocs",
    version=get_version("mkdocs"),
    url='https://www.mkdocs.org',
    project_urls={
        'Source': 'https://github.com/mkdocs/mkdocs',
    },
    license='BSD',
    description='Project documentation with Markdown.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Tom Christie',
    author_email='tom@tomchristie.com',  # SEE NOTE BELOW (*)
    packages=get_packages("mkdocs"),
    include_package_data=True,
    package_data={'mkdocs': ['py.typed']},
    install_requires=[
        'click>=7.0',
        'Jinja2>=2.11.1',
        'Markdown>=3.2.1,<3.4',
        'PyYAML>=5.1',
        'watchdog>=2.0',
        'ghp-import>=1.0',
        'pyyaml_env_tag>=0.1',
        'importlib_metadata>=4.3; python_version < "3.10"',
        'typing_extensions>=3.10; python_version < "3.8"',
        'packaging>=20.5',
        'mergedeep>=1.3.4',
        'colorama>=0.4; platform_system == "Windows"',
    ],
    extras_require={"i18n": ['babel>=2.9.0']},
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'mkdocs = mkdocs.__main__:cli',
        ],
        'mkdocs.themes': [
            'mkdocs = mkdocs.themes.mkdocs',
            'readthedocs = mkdocs.themes.readthedocs',
        ],
        'mkdocs.plugins': [
            'search = mkdocs.contrib.search:SearchPlugin',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        'Topic :: Documentation',
        'Topic :: Text Processing',
    ],
    zip_safe=False,
)

# (*) Please direct queries to the discussion group:
#     https://groups.google.com/forum/#!forum/mkdocs
