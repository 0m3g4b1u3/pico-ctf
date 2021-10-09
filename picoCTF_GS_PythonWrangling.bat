::######################################################################
::	PROGRAM:	Python Wrangling
::	FILENAME:	picoCTF_PythonWrangling.bat
::	AUTHOR:		Om3g4b1u3
::######################################################################
@echo off

set /p pW=<pw_PythonWrangling.txt
python ende.py "-d" flag_PythonWrangling.txt %pW%
