import sqlite3
import os

db_path = 'db.sqlite3'
print("Initializing SQLite Database...")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create signup table
cursor.execute("""
CREATE TABLE IF NOT EXISTS signup (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50),
    contact_no VARCHAR(15),
    email VARCHAR(50),
    address VARCHAR(80)
)
""")

# Create parking_area table
cursor.execute("""
CREATE TABLE IF NOT EXISTS parking_area (
    area_id INTEGER PRIMARY KEY,
    area_name VARCHAR(50),
    direction VARCHAR(50),
    floor_no INTEGER,
    total_slots INTEGER,
    parking_cost DOUBLE
)
""")

# Create book_slot table
cursor.execute("""
CREATE TABLE IF NOT EXISTS book_slot (
    parking_id INTEGER PRIMARY KEY,
    area_id INTEGER,
    slot_no INTEGER,
    entry_date VARCHAR(40),
    exit_date TIMESTAMP,
    total_charges DOUBLE,
    vehicle_no VARCHAR(40),
    username VARCHAR(50),
    card_no VARCHAR(20),
    cvv_no VARCHAR(5),
    status VARCHAR(20)
)
""")

conn.commit()

# Let's seed initial parking area data if it's empty
cursor.execute("SELECT COUNT(*) FROM parking_area")
if cursor.fetchone()[0] == 0:
    print("Seeding initial parking area data...")
    # Add some sample parking areas
    parking_areas = [
        (1, 'Main Gate North', 'North', 1, 10, 15.0),
        (2, 'West Wing A', 'West', 1, 15, 12.0),
        (3, 'Underground B', 'South', -1, 8, 20.0),
        (4, 'Roof Top', 'East', 3, 20, 10.0)
    ]
    cursor.executemany("INSERT INTO parking_area VALUES (?, ?, ?, ?, ?, ?)", parking_areas)
    conn.commit()

# Let's seed an admin signup if it's empty
cursor.execute("SELECT COUNT(*) FROM signup")
if cursor.fetchone()[0] == 0:
    print("Seeding initial signup data...")
    cursor.execute("INSERT INTO signup VALUES ('user', 'user', '1234567890', 'user@example.com', '123 Main St')")
    conn.commit()

print("Database initialized successfully!")
conn.close()
