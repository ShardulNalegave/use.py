#!/usr/bin/env python

"""

	author: Shardul Nalegave
	license:

		MIT License

		Copyright (c) 2018 Shardul Nalegave

		Permission is hereby granted, free of charge, to any person obtaining a copy
		of this software and associated documentation files (the "Software"), to deal
		in the Software without restriction, including without limitation the rights
		to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
		copies of the Software, and to permit persons to whom the Software is
		furnished to do so, subject to the following conditions:

		The above copyright notice and this permission notice shall be included in all
		copies or substantial portions of the Software.

		THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
		IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
		FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
		AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
		LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
		OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
		SOFTWARE.

"""


if __name__ != "__main__":
	from importlib import import_module
	import importlib
	import importlib.util
	import sys
	import os
	from os import path, getcwd as pwd


	class User:
		def __init__(self):
			self.pwd = pwd()
			self.sys_path = sys.path
		def use(self, module_name):
			global sys
			original_module_name = module_name
			if module_name[0] == ".":
				try:
					module_path = path.abspath(path.abspath(path.join(self.pwd, module_name + ".py")))
					while module_name[0] == "." or module_name[0] == "/":
						module_name = module_name[1:]
					module_spec = importlib.util.spec_from_file_location(module_path, module_name + ".py")
					module = importlib.util.module_from_spec(module_spec)
					module_spec.loader.exec_module(module)
					return module
				except AttributeError:
					raise ModuleNotFoundError(f"No Such Module: {original_module_name}")
				except FileNotFoundError:
					raise ModuleNotFoundError(f"No Such Module: {original_module_name}")
				return None
			else:
				try:
					sys.path.remove(self.pwd)
					module = import_module(module_name)
					sys.path.append(self.pwd)
					return module
				except AttributeError:
					raise ModuleNotFoundError(f"No Such Module: {original_module_name}")
				return None


	use = User().use