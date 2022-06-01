import time
from datetime import datetime
from random import random
from typing import Dict

from db import db
from models import TickerChange


current_tickers_state: Dict[str, TickerChange] = {}


def init_state():
    ticker_codes = TickerChange.objects_in(db).only('ticker_code').distinct()
    for ticker_code in ticker_codes:
        initial_ticker_state = TickerChange.objects_in(db).filter(TickerChange.ticker_code == ticker_code.ticker_code)\
            .order_by('-timestamp')[0]
        current_tickers_state[ticker_code.ticker_code] = initial_ticker_state


def run():
    global current_tickers_state
    while True:
        time.sleep(1)
        now = datetime.now()
        new_state: Dict[str, TickerChange] = {}
        for ticker_code in current_tickers_state:
            current_price = current_tickers_state[ticker_code].current_price + generate_movement()
            new_state[ticker_code] = TickerChange(
                ticker_code=ticker_code,
                timestamp=now,
                current_price=current_price,
            )
        db.insert(list(new_state.values()))
        current_tickers_state = new_state


def generate_movement():
    movement = -1 if random() < 0.5 else 1
    return movement


if __name__ == '__main__':
    init_state()
    run()
