"""\
This script takes a name as a command line argument and prints a greeting to the user
Usage: HelloUser.py NAME
"""

# import the python System library (named 'sys')
import sys

# get the command line arguments (minus the 1st arg - filename)
cmdLnArgArray = sys.argv[1:]

# print Hello + input
print("Hello " + cmdLnArgArray[0])
