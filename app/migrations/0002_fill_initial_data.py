from datetime import datetime

from infi.clickhouse_orm import migrations

from models import TickerChange


def fill_db(database):
    now = datetime.now()
    database.insert([TickerChange(
        ticker_code=f'ticker_{i:02}',
        timestamp=now,
        current_price=0,
    ) for i in range(100)])


operations = [
    migrations.RunPython(fill_db),
]
