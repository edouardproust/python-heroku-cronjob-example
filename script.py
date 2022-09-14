#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from os.path import exists
from datetime import datetime

FILE = "/home/sygno/Sites/www/buffalert/cron/output.txt"

def writedate():

    line = 1
    if exists(FILE):
        file = open(FILE, "r") 
        lines = file.readlines()
        line = len(lines) + 1

    file = open(FILE, "a") 
    date = str(line) + ': Cronjob executed on ' + datetime.now().strftime('%A %d-%m-%Y, %H:%M:%S') + '\n'
    file.write(date)
    file.close()

if __name__ == '__main__':
    writedate()