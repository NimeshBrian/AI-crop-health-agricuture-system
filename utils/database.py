import sqlite3
import os
from datetime import datetime

# Database file path configuration (saves crop_history.db in project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'crop_history.db')

def init_db():
    """
    Initialize SQLite database and create history table if it doesn't exist.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            disease TEXT NOT NULL,
            irrigation TEXT NOT NULL,
            severity TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_record(disease, irrigation, severity):
    """
    Save a new prediction record into the history table.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO history (date, disease, irrigation, severity)
        VALUES (?, ?, ?, ?)
    ''', (current_time, disease, irrigation, severity))
    conn.commit()
    conn.close()

def get_history(limit=10):
    """
    Retrieve the latest records from the history table for dashboard display.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT date, disease, irrigation, severity
        FROM history
        ORDER BY id DESC
        LIMIT ?
    ''', (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    # Test script: Initialize DB, insert a dummy record, and fetch history
    init_db()
    save_record(disease="Tomato Early Blight", irrigation="High", severity="Moderate")
    records = get_history()
    print("Database initialized and sample record saved successfully.")
    print("Recent History Records:", records)