
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Print Simple Sum Function',
    'author': 'mrech',
    'url': 'URL to get it at:',
    'author_email': '@mail.el',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex46_sum'],
    'scripts': ['bin/bin_sum.py'],
    'name': 'ex46_sum'
}

setup(**config)
