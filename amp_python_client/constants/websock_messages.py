############
# Channels #
############

ORDERS = "orders"
OHLCV = "ohlcv"
ORDERBOOK = "orderbook"
RAW_ORDERBOOK = "raw_orderbook"
TRADES = "trades"

############
# Messages #
############


# Common Messages

INIT = "INIT"
UPDATE = "UPDATE"

# TRADES messages

SUBSCRIBE_TRADES = "SUBSCRIBE_TRADES"
UNSUBSCRIBE_TRADES = "UNSUBSCRIBE_TRADES"

# ORDERBOOK messages

SUBSCRIBE_ORDERBOOK ="SUBSCRIBE_ORDERBOOK"
UNSUBSCRIBE_ORDERBOOK = "UNSUBSCRIBE_ORDERBOOK"

# OHLCV messages

SUBSCRIBE_OHLCV = "SUBSCRIBE_OHLCV"
UNSUBSCRIBE_OHLCV = "UNSUBSCRIBE_OHLCV"



def base_message():
    return """
    {
      "channel": <channel_name>,
      "event": {
        "type": <event_type>,
        "payload": <payload>
      }
    }
    """
