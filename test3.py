import os
import subprocess

cmd = ['ls']
#subprocess.run(cmd)

dir = 'Data'
file = 'test.py'
location = './' + dir + '/' + file
print(location)