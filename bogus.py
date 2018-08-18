#!/usr/bin/python
import string
import random
import os

contents = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

with open("./proof.txt", "w") as theFile:
    theFile.write(contents)
    theFile.write("\n")

commitCmd = "git commit -am 'new commit %s'" % contents

os.system(commitCmd)
os.system("git push")

