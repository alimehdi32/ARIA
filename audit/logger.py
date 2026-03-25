import sqlite3
from datetime import datetime

conn = sqlite3.connect("audit.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    agent TEXT,
    event TEXT,
    payload TEXT
)
""")

conn.commit()


class AuditLogger:
    def log(self, agent, event, payload):
        timestamp = datetime.utcnow().isoformat()

        cursor.execute(
            "INSERT INTO logs (timestamp, agent, event, payload) VALUES (?, ?, ?, ?)",
            (timestamp, agent, event, str(payload))
        )
        conn.commit()

        print(f"[AUDIT] {timestamp} | {agent} | {event}")
