import os,binascii

def generateUUID():
    ''' generate random ascii string of length 20'''
    return str(binascii.b2a_hex(os.urandom(10))
