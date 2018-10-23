class MessageSchema(object):

    """
    Provides subscription frame and validation for subscribed
    """

    # Although it would be less verbose, the schemas are meant to also work as
    # a validation layer and all fields included are flagged Required by the API.

    def subscribeTrades(self, _base_token_addr, _quote_token_addr, _base_token_symbol, _quote_token_symbol):

        frame = {
         "channel": "trades",
            "event": {
              "type": "SUBSCRIBE",
              "payload": {
                "baseToken": _base_token_addr,
                "name": "%s/%s" % (_base_token_symbol, _quote_token_symbol),
                "quoteToken": _quote_token_addr
              }
            }
          }

        return frame

    def unsubscribeTrades(self):

        frame = {
          "channel": "trades",
          "event": {
          "type": "UNSUBSCRIBE",
          }
        }
        return frame


    def subscribeOrderBookMessage(self, _base_token_addr, _quote_token_addr, _base_token_symbol, _quote_token_symbol):

        frame = {
          "channel": "orderbook",
          "event": {
            "type": "SUBSCRIBE",
            "payload": {
              "baseToken": _base_token_addr,
              "quoteToken": _quote_token_addr,
              "name": "%s/%s" % (_base_token_symbol, _quote_token_symbol),
            }
          }
        }

        return frame


    def unsubscribeOrderBookMessage(self):

        frame = {
          "channel": "orderbook",
          "event": {
            "type": "UNSUBSCRIBE",
          }
        }

        return frame


    def subscribeCandlestickMessage(self,
                                    _to,
                                    _from,
                                    _duration,
                                    _units,
                                    _base_token_address,
                                    _quote_token_address,
                                    _base_token_symbol,
                                    _quote_token_symbol):

        frame = {
          "channel": "ohlcv",
          "event": {
            "type": "SUBSCRIBE",
            "payload": {
              "baseToken": _base_token_address,
              "quoteToken": _quote_token_address,
              "name": "%s/%s" % (_base_token_symbol, _quote_token_symbol),
              "from": _from,
              "to": _to,
              "duration": _duration,
              "units": _units
            }
          }
        }


        pass


    def unsubscribeCandlestickMessage(self):

        frame = {
          "channel": "ohlcv",
          "event": {
            "type": "UNSUBSCRIBE",
          }
        }


        return frame


    def newOrder(self, _orderhash, _order):

        frame = {
          "channel": "orders",
          "event": {
            "type": "NEW_ORDER",
            "hash": _orderhash,
            "payload": _order,
          }
        }

        return frame


    def cancelOrder(self, _hash, _order_hash, _signature):

        frame = {
          "channel": "orders",
          "event": {
            "type": "CANCEL_ORDER",
            "hash": _hash, # will get deprecated i think
            "payload": {
              "hash": _hash,
              "orderHash": _order_hash,
              "signature": _signature,
            }
          }
        }

        return frame


    def submitSignature(self, _order_hash, _order, _remaining_order, _matches_array):
        """
            SAMPLE_MATCHES_ARRAY = [
              {
                "order": <order>,
                "trade": <trade>
              },
              {
                "order": <order>,
                "trade": <trade>
              },
              #...
            ]
        """

        frame = {
          "channel": "orders",
          "event": {
            "type": "SUBMIT_SIGNATURE",
            "hash": _order_hash,
            "payload": {
              "order": _order,
              "remainingOrder": _remaining_order,
              "matches": _matches_array
            }
          }
        }

        return frame
