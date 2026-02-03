from logger import log_info

portfolio = {}

def update_portfolio(pair_name, liquidity_usd, fees_earned):
    if pair_name not in portfolio:
        portfolio[pair_name] = {"liquidity": 0, "fees": 0}
    portfolio[pair_name]["liquidity"] += liquidity_usd
    portfolio[pair_name]["fees"] += fees_earned
    log_info(f"Portfolio updated: {pair_name} liquidity={portfolio[pair_name]['liquidity']}, fees={portfolio[pair_name]['fees']}")

def get_portfolio_summary():
    summary = ""
    for pair, data in portfolio.items():
        summary += f"{pair}: Liquidity=${data['liquidity']}, Fees=${data['fees']}\n"
    return summary
