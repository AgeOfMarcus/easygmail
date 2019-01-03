import setuptools
import os

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(name='easygmail',
	version='0.0.1',
	description='A python library for easily sending and recieving emails from Gmail.',
	long_description=read("README.md"),
	url='https://github.com/AgeOfMarcus/easygmail',
	author='Marcus Weinberger',
	author_email='marcus@marcusweinberger.com',
	license='GPL',
	packages=setuptools.find_packages(),
	zip_safe=False,
	install_requires=[
		
	])
