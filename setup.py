#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import setup

setup(
    name='certbot_adc',
    version='0.1',
    description="perform certbot auto dns challenge with DNS provider's API",
    url='http://github.com/btpka3/certbot-auto-dns-challenge',
    author='btpka3',
    author_email='btpka3@163.com',
    license='Apache License v2.0',
    packages=['certbot_adc'],
    install_requires=[
        "aliyun-python-sdk-core>=2.0.7",
        "aliyun-python-sdk-alidns>=2.0.7",
        "PyYAML>=3.12",
        "validate_email>=1.3"
    ],
    scripts=[
        'bin/certbot-adc-check-conf',
        'bin/certbot-adc-manual-auth-hook'
    ],
    zip_safe=False
)
