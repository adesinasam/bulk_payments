# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in bulk_payments/__init__.py
from bulk_payments import __version__ as version

setup(
	name='bulk_payments',
	version=version,
	description='Bulk Payments Entry for ERPNext',
	author='Glistercp',
	author_email='support@glistercp.com.ng',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
