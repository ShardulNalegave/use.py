
from setuptools import setup

setup(

	name="use",
	description="A Library For Dynamically Importing Modules. Inspired By **Node.js** `require` Function.",
	long_description=open("./README.md", "r").read(),
	long_description_content_type="text/markdown",
	version="0.1.0",
	url="https://github.com/ShardulNalegave/use.py",
	author="Shardul Nalegave",
	author_email="nalegaveshardul40@gmail.com",
	license="MIT",
	packages=["use"],
	classifiers=[
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: Implementation :: CPython",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Operating System :: OS Independent",
		"Topic :: Utilities"
	]

)