from web3 import Web3
from decimal import Decimal

def wei_to_decimal(amount, decimals):
    return Decimal(amount) / (10 ** decimals)

def decimal_to_wei(amount, decimals):
    return int(amount * (10 ** decimals))

def get_current_price(pair_contract):
    slot0 = pair_contract.functions.slot0().call()
    sqrt_price_x96 = slot0[0]
    price = (sqrt_price_x96 ** 2) / (2 ** 192)
    return price
