from fastapi import FastAPI
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_logs():
    conn = sqlite3.connect("audit.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 20")
    rows = cursor.fetchall()

    logs = []
    for row in rows:
        logs.append({
            "id": row[0],
            "timestamp": row[1],
            "agent": row[2],
            "event": row[3],
            "payload": row[4]
        })

    return logs


@app.get("/logs")
def fetch_logs():
    return {"logs": get_logs()}