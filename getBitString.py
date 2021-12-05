from rflib import *
import sys, bitstring

def init(device):
        device.setMdmModulation(MOD_ASK_OOK)
        device.setFreq(315000000)
        device.setMdmSyncMode(0x00)
        device.setMdmNumPreamble(0)
        device.setPktPQT(0)
        device.setMaxPower()
        device.setMdmDRate(6500)

def get_bitstring(*symbols):
        bs = ''
        for s in symbols:
                if s > 0:
                        bs += '1'
                else:
                        bs += '0'
        print(bs)

def bits2bytes(bit_string):
        return bitstring.BitArray(bin=str(bit_string.strip())).tobytes()

def xmit(bit_string):
        try:
                d.RFxmit((bits2bytes(bit_string)) * 10)
        except ChipconUsbTimeoutException:
                pass
        except:
                print("Invalid bit string or xmit error")
                sys.exit()
