
# @ Author: David Van Isacker

"""



import { utils } from 'ethers'
import { getOrderHash, getOrderCancelHash, getTradeHash, getRandomNonce } from '../../../utils/crypto'
import { EXCHANGE_ADDRESS } from '../../../config/contracts'
import { round } from '../../../utils/helpers'

export const signOrder = async function(order) {
  order.hash = getOrderHash(order)

  let signature = await this.signMessage(utils.arrayify(order.hash))
  let { r, s, v } = utils.splitSignature(signature)

  order.signature = { R: r, S: s, V: v }
  return order
}

export const signTrade = async function(trade) {
  trade.hash = getTradeHash(trade)

  let signature = await this.signMessage(utils.arrayify(trade.hash))
  let { r, s, v } = utils.splitSignature(signature)

  trade.signature = { R: r, S: s, V: v }
  return trade
}


export const createOrderCancel = async function(orderHash) {
  let orderCancel = {}
  orderCancel.orderHash = orderHash
  orderCancel.hash = getOrderCancelHash(orderCancel)

  let signature = await this.signMessage(utils.arrayify(orderCancel.hash))
  let { r, s, v } = utils.splitSignature(signature)
  orderCancel.signature = { R: r, S: s, V: v }

  return orderCancel
}
"""


def createRawOrder (_user_address, _exchange_addr, _side, _pair_obj, _amount, _price, _make_fee, _take_fee):
    order = {}
    base_token_addr = pair.get("baseTokenAddress")
    quote_token_addr = pair.get("quoteTokenAddress")

    #let exchangeAddress = EXCHANGE_ADDRESS[this.provider.network.chainId]
  
    # The amountPrecisionMultiplier and pricePrecisionMultiplier are temporary multipliers
    # that are used to turn decimal values into rounded integers that can be converted into
    # big numbers that can be used to compute large amounts (ex: in wei) with the amountMultiplier
    # and priceMultiplier. After multiplying with amountMultiplier and priceMultiplier, the result
    # numbers are divided by the precision multipliers.
    # So in the end we have:
    # amountPoints ~ amount * amountMultiplier ~ amount * 1e18
    # pricePoints ~ price * priceMultiplier ~ price * 1e6

    amountPrecisionMultiplier = 1e6
    pricePrecisionMultiplier = 1e6
    amountMultiplier = 1e18
    priceMultiplier = 1e6
    amount = round(amount * amountPrecisionMultiplier)
    price = round(price * pricePrecisionMultiplier)

    amountPoints = (_amount * amountMultiplier) / amountPrecisionMultiplier

    pricePoints = (price * priceMultiplier) / pricePrecisionMultiplier

    order["userAddress"] = _user_address
    order["exchangeAddress"] = _exchange_addr

    order["buyToken"] = base_token_addr if side == 'BUY' else quote_token_addr
    order["buyAmount"] = str(amountPoints) if side == 'BUY' else str((amountPoints * pricePoints) / priceMultiplier)

    order["sellToken"] = quote_token_addr if side == 'BUY' else base_token_addr
    order["sellAmount"] = str((amountPoints * pricePonts) / priceMultiplier) if side == 'BUY' else str(amountPoints)

    order["makeFee"] = _make_fee
    order["takeFee"] = _take_fee
    order["nonce"] = getRandomNonce() # from crypto
    order["expires"] = '10000000000000'
    order["hash"] = getOrderHash(order)


    # TODO: Finish porting this
    signature = signMessage(utils.arrayify(order.hash))
    r, s, v  = utils.splitSignature(signature)
    order.signature = { R: r, S: s, V: v }

    return order
