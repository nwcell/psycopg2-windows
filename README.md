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
pip install -e git+git@github.com:nwcell/psycopg2-windows.git@win32-py2.5#egg=psycopg2
```
###### Python 2.6
```
pip install -e git+git@github.com:nwcell/psycopg2-windows.git@win32-py2.6#egg=psycopg2
```
###### Python 2.7
```
pip install -e git+git@github.com:nwcell/psycopg2-windows.git@win32-py2.7#egg=psycopg2
```
###### Python 3.2
```
pip install -e git+git@github.com:nwcell/psycopg2-windows.git@win32-py3.2#egg=psycopg2
```
###### Python 3.3
```
pip install -e git+git@github.com:nwcell/psycopg2-windows.git@win32-py3.3#egg=psycopg2
```
#### Windows 64 bit
###### Python 2.6
```
pip install -e git+git@github.com:nwcell/psycopg2-windows.git@win64-py2.6#egg=psycopg2
```
###### Python 2.7
```
pip install -e git+git@github.com:nwcell/psycopg2-windows.git@win64-py2.7#egg=psycopg2
```
###### Python 3.2
```
pip install -e git+git@github.com:nwcell/psycopg2-windows.git@win64-py3.2#egg=psycopg2
```
###### Python 3.3
```
pip install -e git+git@github.com:nwcell/psycopg2-windows.git@win64-py3.3#egg=psycopg2
```

Credits
-------
 - [Me (AKA: Travis Krause)](http://codeforemen.com): Pipified stuff....  Wrote these docs too...
 - [Jason Erickson](http://www.stickpeople.com): Did the legwork and compiled everything

Liscense
--------
Same as [Psycopg2](http://initd.org/psycopg/license/)