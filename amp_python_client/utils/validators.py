import re
import hashlib
import sha3

def is_valid_ethereum_address(_addr):
    return bool(re.compile("^0x[a-fA-F0-9]{40}$").find(_addr))
