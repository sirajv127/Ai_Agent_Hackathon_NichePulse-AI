import sqlite3

DATABASE_FILE = "nichepulse.db"

def init_db():
    """Initializes the database and creates tables if they don't exist."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    # Create reports table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY,
        date_range TEXT NOT NULL,
        generated_brief TEXT NOT NULL
    )
    """)
    
    # Create influencers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS influencers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        handle TEXT NOT NULL,
        platform TEXT NOT NULL
    )
    """)
    
    conn.commit()
    conn.close()
    print("Database initialized successfully.")