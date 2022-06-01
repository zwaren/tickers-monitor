from infi.clickhouse_orm import Model, StringField, DateTimeField, Int32Field, MergeTree


class TickerChange(Model):
    ticker_code = StringField()
    timestamp = DateTimeField()
    current_price = Int32Field()

    engine = MergeTree('timestamp', ('ticker_code', 'current_price'))
