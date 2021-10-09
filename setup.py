import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Most_Active_Cookie",
    version = "0.0.1",
    author = "Kevin Xu",
    author_email = "xukev@seas.upenn.edu",
    description = ("Most_Active_Cookie is a csv parsing script that returns the most active cookies on a particular day"),
    license = "CC-BY-NC-SA",
    keywords = "csv parser cookies",
    url = "https://github.com/kxu112/Quantcast_Challenge/",
    packages=[],
    long_description=read('README.md'),
    scripts=['bin/most_active_cookies'],
)