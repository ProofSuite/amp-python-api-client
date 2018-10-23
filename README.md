# amp-python-api-client
A simple AMP client with interfaces to an instance of the AMP decentralized exchange

This is a simple python client for the AMP Decentralized Exchange API.
It provides a simple interface utilizing Python types for accessing
various functions on the AMP API.  Given that the API itself is in
development, this client-lib will be changing rapidly and we do not
recommend utilizing it yet for production-level code.

# Installation
The AMP Python client requires a version **>=3.6 Python**. We also
**STRONGLY** recommend setting up a virtualenv with a lib prior to implementing
the client.  We will be submitting to the PyPi index as soon as the codebase
matures to a beta-level state.

```python
pip install requirements.txt
```

Likewise Testing Endpoints for the AMP API can be found at

## http://13.125.100.61:8081

NOTE: Up until 2018 December the API itself will also be spotty so This
client lib may have strange behavior at times.

# Developer Notes

At initial commit this is still a very early version of the client.  Since the
API is still in development and the exchange itself is in a constant state of
flux.

### TO DO



* Create a set of sample apps and write more comprehensive documentation for
client code.

* Build a ClientHelper class that includes methods for signing, broadcasting, and modifying orders amongst others for EASE OF USE.

* Implement web3 methods for interfacing with the smart contract (This will
  be placed in a separate clientUtil library since it isn't a functionality of the API itself.)

* Subclass WebSocket type from websocket-client

* Add more stream helpers to the socket pipe

* Implement custom session object for more advanced calls after API auth logic is implemented

* Read off of pipe to synchronize socket thread behavior

* Implement future-proof async methods for socket requests

* Add in an eth validator for all address args

* DRY-ify RESTful after the api gets finalized

* Create custom request object for  api-requesting engines

* Write validator classes in socket-message schema

* After API has matured write a setup.py file and submit to PyPi

* tests!


### Known Issues and Bugs

Well... where do we start?

* Websocket runtime errors fail silently if a client method is incorrectly implemented (this should be optional behavior)

* Since we are using composition the binding of methods from instanced objects is a bit dirty but lends itself to a high level of extensibility.  This is a tradeoff to be considered...

* Many endpoints are largely untested so usage may be spotty.

* So many more...

# Usage example

```python
from amp_python_client import AmpClient

SAMPLE_HOST = "13.125.100.61"
SAMPLE_PORT = "8081"

def sample_callback(_msg): # REQUIRES callback for handling real-time messages from socket
    print(_msg)

Client = AmpClient(SAMPLE_HOST, SAMPLE_PORT)

# Restful Example

Client.getAllPairs

# Socket Example

Client.createSocket(sample_callback)
Client.subscribeTrades()
```


# Available Methods:

## RESTful Interfaces

```
getAccount(_user_address)


getTokenAtAddress(_user_address, _token_address)


# Pair Methods

getAllPairs()


getSinglePair(_base_token, _quote_token)


getPairData(_base_token, _quote_token)


# Tokens Methods

getRegisteredTokens()


getRegisteredBaseTokens()


getRegisteredBaseTokens()


getTokensAtAddress(_user_address)


# Orderbook Methods

getOrderBookDepthOnPair(_base_token, _quote_token)


getFullOrderBookOnPair(_base_token, _quote_token)


# Trade Info Methods

getTradeListOnAddress(_user_address)

getAllTradesOnToken(_base_token, _quote_token)


# Order Methods

getAllOrdersOnAddress(self, _user_address)


getAllPositionsOnAddress(_user_address)


getAllFilledOrdersOnAddress(_user_address)


getCandlestickData(_base_token, _quote_token,
                       _pair_name, _unit, _duration,
                       _from, _to)

```


## Socket Interfaces


```

subscribeTrades(_base_token_addr, _quote_token_addr, _base_token_symbol, _quote_token_symbol)


unsubscribeTrades()


subscribeOrderBookMessage(_base_token_addr, _quote_token_addr, _base_token_symbol, _quote_token_symbol)


unsubscribeOrderBookMessage()

subscribeCandlestickMessage(_to, _from, _duration, _units, _base_token_address, _quote_token_address, _base_token_symbol, _quote_token_symbol)


unsubscribeCandlestickMessage()

newOrder(_orderhash, _order)

cancelOrder(_hash, _order_hash, _signature):

submitSignature(_order_hash, _order, _remaining_order, _matches_array)
```
