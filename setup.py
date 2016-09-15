try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'MUD Engine',
    'author': 'Slava',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'horlet@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['dungeon'],
    'scripts': [],
    'name': 'Dungeon'
}

setup(**config)
