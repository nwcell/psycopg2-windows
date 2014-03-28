@ECHO OFF
setlocal EnableDelayedExpansion
echo ========================
echo Building environments to test
echo ========================
for %%d in (win32-py27 win32-py32 win32-py33 win64-py27 win64-py32 win64-py33) do (
   @ECHO OFF
   echo ------------------------
   virtualenv --no-site-packages  --clear --python=%cd%\pythons\%%d\python.exe %%d
   %cd%\%%d\Scripts\pip install -e git+git@github.com:nwcell/psycopg2-windows.git@%%d#egg=psycopg2
)
echo ------------------------
cls
echo ========================
echo Testing environments
echo ========================
for %%d in (win32-py27 win32-py32 win32-py33 win64-py27 win64-py32 win64-py33) do (
   @ECHO OFF
   %cd%\%%d\Scripts\python test.py
)
for %%d in (win32-py27 win32-py32 win32-py33 win64-py27 win64-py32 win64-py33) do (
   @ECHO OFF
   rmdir /s /q %cd%\%%d
)
@ECHO ON