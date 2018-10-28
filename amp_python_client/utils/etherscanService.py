from requests import get

endpoints =
{
    "get_norm_transactions" : "http://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock={startblock}&endblock={endblock}"
    "get_internal_transactions" : "http://api.etherscan.io/api?module=account&action=txlistinternal&address={address}&startblock={startblock}&endblock={endblock}"
}

class EtherscanService(object):

    def getNormalTransactions(self, _addr, _start_block = 0, _end_block = 9999999999):
        ep = endpoints.get("get_norm_transactions").format(address = _addr, startblock = _start_block, endblock = _end_block)
        resp = get(ep)
        return resp.json()

    def getInternalTransactions(self, _addr, _start_block = 0, _end_block = 9999999999):
        ep = endpoints.get("get_internal_transactions").format(address = _addr, startblock = _start_block, endblock = _end_block)
        resp = get(ep)
        return resp.json()
