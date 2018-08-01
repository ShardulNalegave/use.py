
# Use
A Library For Dynamically Importing Modules. Inspired By **Node.js** `require` Function.


-----------------------------------------------------------------------------------------------------------


## Installation
Use can be installed using Pip by the command:-


````

    [sudo] pip install use

````


## Usage
If the file structure is like:-

````

    test/
    	test/
    		__init__.py
    		test.py
    		utils/
    			__init__.py
    			utils.py

````

If you want to import `test/test/__init__.py` in the file `test/test/utils/utils.py` it is not possible, but using **Use** you can do it by putting the following snippet in `test/test/utils/utils.py` file.

````

    from use import use

    initFile = use("./../__init__")

````


-----------------------------------------------------------------------------------------------------------


**License Under The [MIT](./LICENSE) License**
**A Project By [Shardul Nalegave](https://shardul.netlify.com)**