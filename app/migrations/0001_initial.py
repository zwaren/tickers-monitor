from infi.clickhouse_orm import migrations

from models import TickerChange

operations = [
    migrations.CreateTable(TickerChange),
]
