# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger()
import subprocess
import time
import datetime

def execute(profile, path, command):
    cmd = "sudo vol.py --profile=" + profile + " " + path + " " + command
    logger.info("start cmd: " + cmd)

    d1 = datetime.datetime.now()
    fileAns = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).stdout.read()
    d2 = datetime.datetime.now()

    with open("profile="+profile+" "+path[1]+" "+command, "w") as f:
        f.write("start cmd: " + cmd + " " + str(d1) + "\n")
        f.write("end cmd: " + cmd + " " + str(d2) + "\n")
        f.write("use time: " + str(d2 - d1) + "\n")

        for line in fileAns:
            f.write(line)



    logger.info("end cmd:" + cmd + " \nuse time: " + str(d2 - d1))
