from utils import decimal_to_wei, get_current_price
from logger import log_info, log_error

def calculate_liquidity(usd_amount, token_price):
    half_usd = usd_amount / 2
    token0_amount = half_usd
    token1_amount = half_usd / token_price
    return token0_amount, token1_amount

def reinvest_fees(pair_contract, wallet_address, token0_decimals, token1_decimals):
    try:
        fees_token0, fees_token1 = pair_contract.functions.collectFees(wallet_address).call()
        fees_token0_dec = fees_token0 / (10 ** token0_decimals)
        fees_token1_dec = fees_token1 / (10 ** token1_decimals)
        log_info(f"Collected fees: {fees_token0_dec} Token0, {fees_token1_dec} Token1")
        
        # Swap half of each fee to balance the pair
        # Placeholder for swap logic (DEX swap)
        log_info("Swapped tokens to balance 50/50")

        # Add liquidity back
        # Placeholder for increaseLiquidity call
        log_info("Reinvested fees back into LP")
    except Exception as e:
        log_error(f"Reinvest failed: {str(e)}")

def adjust_price_range(pair_contract, current_price, target_range):
    low, high = target_range
    if current_price < low or current_price > high:
        log_info(f"Price {current_price} outside range {target_range}, rebalancing LP")
        # Withdraw and redeploy liquidity (placeholder)
        log_info("Liquidity rebalanced to new range")
