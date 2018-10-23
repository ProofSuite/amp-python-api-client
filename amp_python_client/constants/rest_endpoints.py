
# Restful Interfaces

# Account Resources

GET_ADDRESS = "/account/{userAddress}"
GET_TOKEN_AT_ADDRESS = "/account/{userAddress}/{tokenAddress}"

# Pairs Resources

GET_ALL_PAIRS = "/pairs"
GET_SINGLE_PAIR = "/pair?baseToken={baseToken}&quoteToken={quoteToken}"
GET_PAIR_DATA= "/pairs/data?baseToken={baseToken}&quoteToken={quoteToken}"

# Token Resources

GET_REGISTERED_TOKENS = "/tokens"
GET_REGISTERED_BASE_TOKENS = "/tokens/base"
GET_REGISTERED_QUOTE_TOKENS = "/tokens/quote"
GET_TOKENS_AT_ADDRESS = "/tokens/{address}"

# Orderbook resources

GET_ORDERBOOK_DEPTH_ON_PAIR = "/orderbook?baseToken={baseToken}&quoteToken={quoteToken}"
GET_FULL_ORDERBOOK_ON_PAIR = "/orderbook/raw?baseToken={baseToken}&quoteToken={quoteToken}"

# Trade Resources

GET_TRADE_LIST_ON_ADDRESS = "/trades?address={address}"
GET_ALL_TRADES_ON_TOKEN = "/trades/pair?baseToken={baseToken}&quoteToken={quoteToken}"

# Order Resources

GET_ALL_ORDERS_ON_ADDRESS = "/orders?address={address}"
GET_ALL_POSITIONS_ON_ADDRESS = "/orders/positions?address={address}"
GET_ALL_FILLED_ORDERS_ON_ADDRESS = "/orders/history?address={address}"

# OHLCV Resources

GET_OHLCV_DATA = "/ohlcv?baseToken={baseToken}&quoteToken={quoteToken}&pairName={pairName}&unit={unit}&duration={duration}&from={from}&to={to}"

# SOCKET Interfaces
SOCKET = "/socket"
