__author__ = 'Sergey'

import os
import io
from setuptools import setup, find_packages

from nose_ittr.ittr_multiplayer import __version__

here = os.path.abspath(os.path.dirname(__file__))

# workaround for bug in python <= v2.7.3 when using nose.collector
# see http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing
except ImportError:
    pass


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.rst', 'CHANGES.txt')


setup(
    name='nose_ittr',
    version=__version__,
    url='https://github.com/taykey/nose-ittr',
    license='Apache Software License',
    author='Sergey Ragatsky',
    author_email = "serg@taykey.com",
    tests_require=['nose'],
    install_requires=[''],
    description='nose expansion for supporting parametrized testing',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    keywords='nose nosetest docstring metaclass parametrized testing plugin',
    test_suite='nose.collector',
    zip_safe=False,
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Testing',
        ],
     entry_points={
        'nose.plugins.0.10': [
        'setup_ittr = nose_ittr.setup_ittr:SetupIttr'
        ]
    },
)