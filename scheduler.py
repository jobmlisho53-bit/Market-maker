import time
from config import REINVEST_INTERVAL
import bot
from logger import log_info

def schedule_bot():
    while True:
        bot.run_bot()
        log_info(f"Sleeping for {REINVEST_INTERVAL} seconds")
        time.sleep(REINVEST_INTERVAL)

if __name__ == "__main__":
    schedule_bot()
