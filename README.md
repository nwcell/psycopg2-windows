psycopg2-windows
=========
Pip, windows, AND **virtualenv** friendly versions of psycopg2!!!!!   This works because everything is pre-compiled and beautiful.

##### Cool Stuff
* Easy installation of psycopg2 on windows
* Pip install works for windows
* Virtualenv friendly
* No .exe to wrangle with

Why
----
Every time I need to set up psycopg2 on windows, I wind up wanting to shoot something. For years, I've been managing my virtualenv with Jason Erickson's awesome set of pre-compiled [libraries](http://www.stickpeople.com/projects/python/win-psycopg/).  Recently, I decided to quit making my like so difficult and just pipify everything for windows.



Installation Scripts
----
Depending on your environment, you'll want to use the appropriate script.  All downloads are using a **version 2.5.2 of psycopg2**.  Since psycopg2 is for PostgreSQL, you'll obviousely want to have that installed first.

#### Windows 32 bit
###### Python 2.5
```
pip install git+https://github.com/nwcell/psycopg2-windows.git@win32-py25#egg=psycopg2
```
###### Python 2.6
```
pip install git+https://github.com/nwcell/psycopg2-windows.git@win32-py26#egg=psycopg2
```
###### Python 2.7
```
pip install git+https://github.com/nwcell/psycopg2-windows.git@win32-py27#egg=psycopg2
```
###### Python 3.2
```
pip install git+https://github.com/nwcell/psycopg2-windows.git@win32-py32#egg=psycopg2
```
###### Python 3.3
```
pip install git+https://github.com/nwcell/psycopg2-windows.git@win32-py33#egg=psycopg2
```
#### Windows 64 bit
###### Python 2.6
```
pip install git+https://github.com/nwcell/psycopg2-windows.git@win64-py26#egg=psycopg2
```
###### Python 2.7
```
pip install git+https://github.com/nwcell/psycopg2-windows.git@win64-py27#egg=psycopg2
```
###### Python 3.2
```
pip install git+https://github.com/nwcell/psycopg2-windows.git@win64-py32#egg=psycopg2
```
###### Python 3.3
```
pip install git+https://github.com/nwcell/psycopg2-windows.git@win64-py33#egg=psycopg2
```

Tests
----
I've built a primitive test suite that builds python python virtual enviroments and then pip installs psycopg2.  Pip becomes difficult to install starting with python 2.6 and I can't find MSI installs for 2.5.  Because of this, I've not fully tested either of those python versions.  That said, I've put together a .bat file that builds 32 and 63 bit virtualenvs for pythons 2.7, 3.2, and 3.3.  It then installs psycopg2 into each virtualenv.  To keep testing easy, I've included python installations in the tests folder.  I realize that this is not very space sensitive, so the test directory is *only* in the master branch.  Since each compiled version of psycopg2 is kept in a separate branch, installing via pip will not download 6 python installations.

If you *do* want to run the tests themselves, simply clone/checkout master and run tests\scrapt.bat.  From there you may read the scripts output and also check each virtualenv to ensure that the psycopg2 was installed successfully.  If you wan't to help out and have a different environment, please help with the tests.  If you want to help expand the test suite, feel free to help and/or ask any questions.

The test suite assumes that you have a primary python installation with virtualenv already installed.

##### Successfully tested with virtualenv on Windows 7 64 bit:
 - **Windows 32 bit:** Python 2.7
 - **Windows 32 bit:** Python 3.2
 - **Windows 32 bit:** Python 3.3
 - **Windows 64 bit:** Python 2.7
 - **Windows 64 bit:** Python 3.2
 - **Windows 64 bit:** Python 3.3

Credits
-------
 - [Me (AKA: Travis Krause)](http://codeforemen.com): Pipified stuff....  Wrote these docs too...
 - [Jason Erickson](http://www.stickpeople.com): Did the legwork and compiled everything

Liscense
--------
Same as [Psycopg2](http://initd.org/psycopg/license/)
