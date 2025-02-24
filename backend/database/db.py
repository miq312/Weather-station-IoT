import sqlite3

DB_NAME = "temperature_data.db"

def create_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        '''CREATE TABLE IF NOT EXISTS temperature 
        (id INTEGER PRIMARY KEY, value REAL, timestamp 
        DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def save_to_db(temperature):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        '''INSERT INTO temperature (value) VALUES (?)''', (temperature,))
    conn.commit()
    conn.close()

def get_latest_temperatures(limit = 100):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        '''SELECT * FROM temperature ORDER BY id DESC LIMIT ?''', (limit,))
    rows = c.fetchall()
    conn.close()
    return rows