import os
from dotenv import load_dotenv
from web3 import Web3
from logger import log_info, log_error
from config import PAIRS, MIN_LIQUIDITY_USD
from utils import w3, get_current_price
from liquidity_manager import calculate_liquidity, reinvest_fees, adjust_price_range
from portfolio import update_portfolio

load_dotenv()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
INFURA_URL = os.getenv("INFURA_URL")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

w3 = Web3(Web3.HTTPProvider(INFURA_URL))
if not w3.isConnected():
    log_error("Web3 connection failed")
    exit(1)

import json

def load_pair_contract(pair_address, abi_file):
    with open(abi_file) as f:
        abi = json.load(f)
    return w3.eth.contract(address=pair_address, abi=abi)

def run_bot():
    for pair in PAIRS:
        log_info(f"Processing {pair['name']}")
        contract = load_pair_contract(pair["pair_address"], "abi/uniswap_v3_pair.json")
        price = get_current_price(contract)

        adjust_price_range(contract, price, pair["price_range"])
        reinvest_fees(contract, WALLET_ADDRESS, pair["token0_decimals"], pair["token1_decimals"])

        liquidity, fees = calculate_liquidity(MIN_LIQUIDITY_USD, price)
        update_portfolio(pair["name"], liquidity, fees)

    log_info("Portfolio Summary:\n" + update_portfolio.get_portfolio_summary())
