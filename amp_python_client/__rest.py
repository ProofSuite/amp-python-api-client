from .constants import rest_endpoints
import requests # TODO: Fix References to avoid dual imports

class ampRestEndpoints(object):
    # TODO: Add in an eth validator for all address args
    # TODO: DRY-ify this thing after the api gets finalized.  **KWARGS are our friend...
    # TODO: Create custom request object for  api-requesting engines
    # Account Methods
    def __init__(self, _base_endpoint):
        self.base_endpoint = _base_endpoint

    def getAccount(self, _user_address):
        address_endpoint = rest_endpoints.GET_ADDRESS.format(userAddress = _user_address)
        uri = self.base_endpoint + address_endpoint
        return requests.get(uri).json()

    def getTokenAtAddress(self, _user_address, _token_address):
        address_endpoint = rest_endpoints.GET_TOKEN_AT_ADDRESS.format(userAddress = _user_address, tokenAddress = _token_address)
        uri = self.base_endpoint + address_endpoint
        return requests.get(uri).json()

    # Pair Methods

    def getAllPairs(self):
        pair_endpoint = rest_endpoints.GET_ALL_PAIRS
        uri = self.base_endpoint + pair_endpoint
        return requests.get(uri).json()

    def getSinglePair(self, _base_token, _quote_token):
        pair_endpoint = rest_endpoints.GET_SINGLE_PAIR.format(baseToken = _base_token, quoteToken = _quote_token)
        uri = self.base_endpoint + pair_endpoint
        return requests.get(uri).json()

    def getPairData(self, _base_token, _quote_token):
        pair_endpoint = rest_endpoints.GET_PAIR_DATA.format(baseToken = _base_token, quoteToken = _quote_token)
        uri = self.base_endpoint + pair_endpoint
        return requests.get(uri).json()

    # Tokens Methods

    def getRegisteredTokens(self):
        token_endpoint = rest_endpoints.GET_REGISTERED_TOKENS
        uri = self.base_endpoint + token_endpoint
        return requests.get(uri).json()

    def getRegisteredBaseTokens(self):
        token_endpoint = rest_endpoints.GET_REGISTERED_BASE_TOKENS
        uri = self.base_endpoint + token_endpoint
        return requests.get(uri).json()

    def getRegisteredQuoteTokens(self):
        token_endpoint = rest_endpoints.GET_REGISTERED_QUOTE_TOKENS
        uri = self.base_endpoint + token_endpoint
        return requests.get(uri).json()

    def getTokensAtAddress(self, _user_address):
        token_endpoint = rest_endpoints.GET_TOKENS_AT_ADDRESS.format(address = _user_address)
        uri = self.base_endpoint + token_endpoint
        return requests.get(uri).json()

    # Orderbook Methods

    def getOrderBookDepthOnPair(self, _base_token, _quote_token):
        ob_endpoint = rest_endpoints.GET_ORDERBOOK_DEPTH_ON_PAIR.format(baseToken = _base_token, quoteToken = _quote_token)
        uri = self.base_endpoint + ob_endpoint
        return requests.get(uri).json()

    def getFullOrderBookOnPair(self, _base_token, _quote_token):
        ob_endpoint = rest_endpoints.GET_FULL_ORDERBOOK_ON_PAIR.format(baseToken = _base_token, quoteToken = _quote_token)
        uri = self.base_endpoint + ob_endpoint
        return requests.get(uri).json()

    # Trade Info Methods

    def getTradeListOnAddress(self, _user_address):
        trade_endpoint = rest_endpoints.GET_TRADE_LIST_ON_ADDRESS.format(address = _user_address)
        uri = self.base_endpoint + trade_endpoint
        return requests.get(uri).json()

    def getAllTradesOnToken(self, _base_token, _quote_token):
        trade_endpoint = rest_endpoints.GET_ALL_TRADES_ON_TOKEN.format(baseToken = _base_token, quoteToken = _quote_token)
        uri = self.base_endpoint + trade_endpoint
        return requests.get(uri).json()

    # Order Methods

    def getAllOrdersOnAddress(self, _user_address):
        order_endpoint = rest_endpoints.GET_ALL_ORDERS_ON_ADDRESS.format(address = _user_address)
        uri = self.base_endpoint + order_endpoint
        return requests.get(uri).json()

    def getAllPositionsOnAddress(self, _user_address):
        order_endpoint = rest_endpoints.GET_ALL_POSITIONS_ON_ADDRESS.format(address = _user_address)
        uri = self.base_endpoint + order_endpoint
        return requests.get(uri).json()

    def getAllFilledOrdersOnAddress(self, _user_address):
        order_endpoint = rest_endpoints.GET_ALL_FILLED_ORDERS_ON_ADDRESS.format(address = _user_address)
        uri = self.base_endpoint + order_endpoint
        return requests.get(uri).json()

    def getCandlestickData(self, _base_token, _quote_token,
                           _pair_name, _unit, _duration,
                           _from, _to):

        candle_endpoint = rest_endpoints.GET_OHLCV_DATA.format(baseToken = _base_token,
                                                               quoteToken = _quote_token,
                                                               pairName = _pair_name,
                                                               unit = _unit,
                                                               duration = _duration)
        uri = self.base_endpoint + candle_endpoint
        return requests.get(uri).json()
