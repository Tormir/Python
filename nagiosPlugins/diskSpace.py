#librarier

import os
import sys

#script

#used_space=os.popen("df -h / | grep -v Filesystem | awk '{print $5}'").readline().strip()

used_space = "90%"

if used_space < "80%":
        print("OK - " + used_space + " of disk space used.")
        sys.exit(0)
elif "85%" > used_space >= "80%":
        print("WARNING " + used_space + " of disk space used.")
        sys.exit(1)
elif used_space >= "85%":
        print("CRITICAL " + used_space + " of disk space used.")
        sys.exit(2)
else:
        print("UKNOWN " + used_space + " of disk space used.")
        sys.exit(3)