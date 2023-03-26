import os
import subprocess

dir = 'Data'

if os.path.exists(dir) == True:
    for file in os.listdir(dir):
        command = ['python']
        location = './' + dir + '/' + file
        command.append(location)
        subprocess.run(command)
        #print('python ' + file)
else:
    print('No data dir')