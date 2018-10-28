import random

### DECORATORS ###

def hexify(_func): # Decorator to return 0x prefixed strings
    def hex_wrapper(*_args):
        hex_str = _func(*_args)
        return "0x{hexString}".format(hexString = hex_str)
    return hex_wrapper


### FUNCTIONS ###

def simpleSha256(_msg):
    return hashlib.sha256(_msg.encode("utf-8"))

def signK256(*_msg):
    hasher = sha3.keccak_256()

    for _entry in _msg:
        hasher.update(_entry.encode("utf-8"))

    return hasher.hexdigest()

def getRandomNonce():
  return str(random.randint(0, 1e16))

@hexify
def getOrderHash(order):
  return signK256(
      'bytes',
      'bytes',
      'bytes',
      'bytes',
      'uint256',
      'uint256',
      'uint256',
      'uint256',
      'uint256',
      'uint256',
      order.get("exchangeAddress"),
      order.get("userAddress"),
      order.get("sellToken"),
      order.get("buyToken"),
      order.get("sellAmount"),
      order.get("buyAmount"),
      order.get("makeFee"),
      order.get("takeFee"),
      order.get("expires"),
      order.get("nonce")
  )

@hexify
def getOrderCancelHash(order_cancel):
  return signK256('bytes', order_cancel.get(orderHash))

@hexify
def getTradeHash(trade):
  return utils.signK256(
    'bytes',
    'bytes',
    'uint256',
    'uint256',
    trade.get("orderHash"),
    trade.get("taker"),
    trade.get("amount"),
    trade.get("tradeNonce")
  )
