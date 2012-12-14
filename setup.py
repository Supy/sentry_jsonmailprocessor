#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    'sentry>=5.0.21',
    ]

setup(
    name='sentry-smtpforwarder',
    version='0.0.1',
    author='Justin C',
    description='A Sentry extension that forwards Sentry events via SMTP.',
    packages=find_packages(exclude=['test']),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'sentry.plugins': [
            'smtpforwarder = sentry_smtpforwarder.models:Smtpforwarder',
            ],
        },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
