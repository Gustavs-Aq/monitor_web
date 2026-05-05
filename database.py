import sqlite3

DB = "monitor.db"

def get_connection():
    return sqlite3.connect(DB)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS checks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site_id INTEGER,
            status INTEGER,
            tempo REAL,
            data TEXT
        )
    """)

    conn.commit()
    conn.close()