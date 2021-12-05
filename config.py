#!/usr/bin/python3

import rflib

mode = 0

def configRfCat():

    # Start up RfCat
    d = rflib.RfCat()

    # 2010 Toyota Corolla
    if (mode == 0):
        # Set Modulation. We using On-Off Keying here
        d.setMdmModulation(rflib.MOD_ASK_OOK)

        # Configure the radio
        # d.makePktFLEN(len(garbage[0])) # Set the RFData packet length
        d.setMdmDRate(6500)         # Set the Baud Rate
        d.setMdmSyncMode(0)         # Disable preamble
        d.setFreq(315000000)        # Set the frequency
    # 2018 Honda Civic
    elif (mode == 1):
        # Set Modulation. We using On-Off Keying here
        # d.setMdmModulation(rflib.MOD_ASK_OOK)
        d.setMdmModulation(rflib.MOD_2FSK)

        # Configure the radio
        # d.makePktFLEN(len(garbage[0])) # Set the RFData packet length
        # d.setMdmDRate(2702)         # Set the Baud Rate
        # d.setMdmSyncMode(0)         # Disable preamble
        # d.setFreq(315000000)        # Set the frequency
        d.setFreq(433925000)        # Set the frequency
        d.setMdmChanSpc(250000)
        d.setMdmDeviatn(250000)
        d.setMdmChanBW(125000)
    else:
        print("Unknown Mode")
        exit()

    return d
