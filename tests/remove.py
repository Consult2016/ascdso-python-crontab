#!/usr/bin/python

import sys
sys.path.append('../')

import crontab
from crontab import CronTab

t = CronTab()
r = t.remove_all("echo3")
t.write()

