import os
import subprocess

dir = 'Data'

if os.path.exists(dir) == True:
    for file in os.listdir(dir):
        command = 'python ./' + dir + '/' + file
        subprocess.run(str(command))
        #print('python ' + file)
else:
    print('No data dir')