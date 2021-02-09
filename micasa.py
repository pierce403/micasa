#!/usr/bin/python

import binascii
import os
import hashlib
import sys

# INFO: https://en.bitcoin.it/wiki/Mini_private_key_format

### CHANGE THIS TO THE KEY FROM THE BACK OF THE COIN ###

shortkey = "S6c56bnXQiBjk9mqSYE7ykVQ7NzrRy"

##### start code from pywallet.py #############

__b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
__b58base = len(__b58chars)

def b58encode(v):
    """ encode v, which is a string of bytes, to base58.
    """

    long_value = 0L
    for (i, c) in enumerate(v[::-1]):
        long_value += (256**i) * ord(c)

    result = ''
    while long_value >= __b58base:
        div, mod = divmod(long_value, __b58base)
        result = __b58chars[mod] + result
        long_value = div
    result = __b58chars[long_value] + result

    # Bitcoin does a little leading-zero-compression:
    # leading 0-bytes in the input become leading-1s
    nPad = 0
    for c in v:
        if c != '\0': 
            break
        nPad += 1

    return (__b58chars[0]*nPad) + result

def Hash(data):
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def EncodeBase58Check(secret):
    hash = Hash(secret)
    return b58encode(secret + hash[0:4])

########## end code from pywallet.py ############

raw_key = hashlib.sha256(shortkey.encode('utf-8'))
raw_check = hashlib.sha256((shortkey+'?').encode('utf-8'))

print("raw key:   "+raw_key.hexdigest())
print("check key: "+raw_check.hexdigest())

if raw_check.hexdigest()[0:2] != '00':
  print("WARNING!   Checksum failed. Check key should start with '00'")
else:
  print("CONGRATS!  Checksum looks good!")

key_data = binascii.unhexlify('80') + raw_key.digest()
print("\nbtc key:   "+EncodeBase58Check(key_data))
