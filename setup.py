import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='markdown-urlize',
    version='0.2.0',
    description='A more liberal autolink extension for python Markdown',
    long_description=(read('README.md')),
    url='https://github.com/r0wb0t/markdown-urlize',
    license='BSD',
    author='Rowan Nairn',
    author_email='rnairn@gmail.com',
    py_modules=['mdx_urlize'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[ "markdown", ]
)
