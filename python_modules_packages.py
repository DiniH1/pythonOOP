# Python's extensive documentation on python.org
#  We have used funcs that we created as well as built in

import math # to calcuate values
import os
from random import random
# to generate random numbers


# num1 = 23.44
#
# in real life situations you have to round the figure depending on the value
#  if the value is less than .50 round down to 23 if 23.51 then round it up

# print(math.ceil(num1))
# print(math.floor(num1))
#
# # Random class/methods
# print(random())
# generates a random number everytime the prorams executes between 0.0 to .99
# print(math.pi)
import math, datetime, sys #sys is used to get system specific information
work_dir = os.getcwd() # getcwd provides location/path
# print(work_dir)
#
# print(os.getuid())
# print(os.uname())
# print(os.cpu_count())
#
# print(datetime.date.today()) # Today's date
# print(sys.path)
# type() len()

import requests  # requests is a package to interact with a live API -
# we can make API call to any web adress using python requests packages
# pip is a package manager in python to install any packages not available by default
# pip instal requests -

#  pip -v

import requests

requests_api = requests.get("https://www.bbc.co.uk/")
if requests_api.status_code == 200:
    print("Success")
print(type(requests_api.status_code)) # 200 for success 404 and above for failure
print(type(requests_api.headers))
print(type(requests_api.content))