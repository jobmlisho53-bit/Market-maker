# config.py

# List of pairs for multi-pair market making
PAIRS = [
    {
        "name": "PEPE/USDT",
        "pair_address": "0xPEPE_USDT_PAIR_ADDRESS",
        "token0_decimals": 6,
        "token1_decimals": 9,
        "pool_fee": 3000,
        "price_range": (0.000008, 0.00001)
    },
    {
        "name": "SHIB/USDT",
        "pair_address": "0xSHIB_USDT_PAIR_ADDRESS",
        "token0_decimals": 6,
        "token1_decimals": 18,
        "pool_fee": 3000,
        "price_range": (0.000007, 0.000008)
    }
]

MIN_LIQUIDITY_USD = 100       # Minimum liquidity per pair
REINVEST_INTERVAL = 24 * 60 * 60  # 24 hours
GAS_LIMIT = 300_000
