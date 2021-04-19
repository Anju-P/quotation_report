# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in quotation_report/__init__.py
from quotation_report import __version__ as version

setup(
	name='quotation_report',
	version=version,
	description='to generate quotation values',
	author='Momscode Technologies Pvt.Ltd',
	author_email='anju.p@momscode.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
