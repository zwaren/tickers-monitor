import os

from infi.clickhouse_orm import Database


DB_NAME = os.getenv('DB_NAME', 'tickers')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', '18123'))
DB_USER = os.getenv('DB_USER', None)
DB_PASSWORD = os.getenv('DB_PASSWORD', None)

db = Database(DB_NAME, db_url=f'http://{DB_HOST}:{DB_PORT}', username=DB_USER, password=DB_PASSWORD)
db.migrate('migrations')
