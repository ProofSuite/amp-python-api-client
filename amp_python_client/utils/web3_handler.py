import web3
from .eth_utils import contract_abis
from .etherscanService import EtherscanService
# Create Web3 object for passing around

class TokenWrapper(web3.Web3):
    """
    Web3 wrapper
    Returns a collection of objects to simplify the creation and management of
    calls to contracts.
    """

    def isTokenContract(self, _contract_obj):
        pass

    def __init__(self, _contract_addr, _provider, _contract_type = "erc20"):
        web3.Web3.__init__(_provider)
        self.current_abi = contract_abis.get(_contract_type)
        self.current_contract = self.eth.contract(address = _contract_addr, abi = self.current_abi)

    def returnERC20Info(self):
        return {
            "name" : self.current_contract.functions.name() or None,
            "totalSupply" : self.current_contract.functions.totalSupply() or None,
            "decimals" : self.current_contract.functions.decimals() or None,
            "owner" : self.current_contract.functions.owner or None,
            "symbol" : self.current_contract.functions.symbol or None
        }

    def callContract(self,_method):
        return getattr(self.current_contract.functions, _method)

    def availableMethods(self):
        return self.current_contract.functions



class AddressWrapper(web3.Web3):

    def __init__(self, _addr, _provider):
        web3.Web3.__init__(_provider)
        self.ethscan_service = EtherscanService()
        self.address = _addr

    def getAddressNonce(self):
        self.eth.getTransactionCount(self.address)

    def getAllTransactionsOnAddress(self):
        transactions = {}
        normal_transactions = self.ethscan_service.getNormalTransactions(self.address)
        internal_transactions = self.ethscan_service.getInternalTransactions(self.address)

        return {
                "normal" : normal_transactions,
                "internal" : internal_transactions
               }
