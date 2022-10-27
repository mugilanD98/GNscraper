from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='GNscraper',
    version='0.0.1',
    description='GNscraper stands for Google News Scraper which scrape News Articles from Google News based on given Keywords and returns Data Frame which contains Publishers, Title, Url, Uploaded Date and Uploaded DateTime of News Articles.',
    author= 'Mugilan Deiveegan',
    url = 'https://github.com/mugilanD98/GNscraper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['dynamic scraper', 'news scraping','gnews','google news','google news scraper', 'web scraping','GNscraper','web','news','live-scraper'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    py_modules=['GNscraper'],
    package_dir={'':'src'},
    install_requires = [
        'beautifulsoup4',
        'requests',
        'pandas',
        'lxml'
    ]
)

