try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Uses word frequency to find good-fit jobs.',
    'author': 'Michael Thompson',
    'url': 'n/a',
    'download_url': 'n/a',
    'author_email': 'mlthompson5@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['getajob'],
    'scripts': [],
    'name': 'getajob'
}

setup(**config, install_requires=['bs4', 'requests'])
