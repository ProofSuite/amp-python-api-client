import re
import hashlib
import sha3

def is_valid_ethereum_address(_addr):
    return bool(re.compile("^0x[a-fA-F0-9]{40}$").find(_addr))

def simpleSha256(_msg):
    return hashlib.sha256(_msg.encode("utf-8"))

def signK256(_msg):
    return sha3.keccak_256(_msg.encode("utf-8"))
