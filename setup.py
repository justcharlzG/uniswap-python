#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="uniswap-python",
    version="0.0.0",
    author="Shane Fontaine",
    author_email="shane6fontaine@gmail.com",
    license='MIT',
    description="An unofficial python wrapper for the Uniswap exchange",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shanefontaine/uniswap-python",
    packages=find_packages(),
    keywords=['uniswap', 'uniswap-exchange', 'uniswap-api', 'orderbook', 'dex',
              'trade', 'ethereum', 'ETH', 'client', 'api', 'wrapper',
              'exchange', 'crypto', 'currency', 'trading', 'trading-api',
              'decentralized-exchange'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "Programming Language :: Python :: 3.6",
    ],
)