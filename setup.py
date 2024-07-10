"""Module providing info about the package and its dependencies."""

from setuptools import setup, find_packages

setup(
    name='multiaihub',
    version='0.1.0',  # Start with a version number
    description='Short description of your project',
    license='Apache License 2.0',
    long_description="MAH - Multi AI Hub is a project designed to make it easy to send the same prompt to multiple LLMs to help with testing and comparison.",
    author='Mike Wolfson',
    author_email='mike@ableandroid.com',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
        'google.generativeai',
        'openai',
        'anthropic',
    ],
)
