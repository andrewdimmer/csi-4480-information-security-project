#!/usr/bin/python3

import rflib
import config
import time

d = config.configRfCat()
d.discover()
time.sleep(1)
d.setModeIDLE()

print("Exit")
