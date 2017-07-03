#Checking for file existence with glob.glob

import glob
import os
os.chdir("/home/skeer/Documents/Projects/Python_temp/home/adr01/upload/")
for file in glob.glob("*.pgp"):
# You can print the filename
    print(file)
# Or pass to a list
monitor_files.append(file)