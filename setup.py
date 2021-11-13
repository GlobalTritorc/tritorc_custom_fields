from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tritorc_custom_fields/__init__.py
from tritorc_custom_fields import __version__ as version

setup(
	name="tritorc_custom_fields",
	version=version,
	description="Custom fields for Tritorc India",
	author="Firsterp",
	author_email="support@fristerp.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
