from setuptools import setup, find_packages

setup(
    name = 'twitter-news-bot',
    version = '0.1',
    author = 'Eric Connelly',
    description = 'A Twitter Bot to tweet about curated news content',
    url = 'https://github.com/econne01/twitter-news-bot',
    install_requires = [
        'oauth2>=1.9,<2',
        'requests>=2.9,<3.0'
    ],
    packages = find_packages(),
)
