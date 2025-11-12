import sqlite3
from pathlib import Path
class Database:
    def __init__(self, db_path):
        p = Path(db_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(p))
        self._ensure_tables()
    def _ensure_tables(self):
        c = self.conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS events(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts DATETIME DEFAULT CURRENT_TIMESTAMP,
            type TEXT,
            payload TEXT
        )""")
        self.conn.commit()
    def insert_event(self, type_, payload):
        c = self.conn.cursor()
        c.execute("INSERT INTO events(type,payload) VALUES(?,?)", (type_, payload))
        self.conn.commit()
