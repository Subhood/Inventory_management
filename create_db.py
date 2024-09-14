# create_db.py
import sqlite3

def create_inventory_table():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    
    # Create table
    c.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_inventory_table()
