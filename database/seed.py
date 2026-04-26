import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def create_seed_data(conn):
    """ create seed data for testing
    :param conn: Connection object
    :return:
    """

    # Create a cursor object
    cur = conn.cursor()

    # Insert into Categories table
    categories = [
        ('Food',),
        ('Retail',),
        ('Services',),
        ('Entertainment',),
        ('Health and Wellness',),
    ]
    cur.executemany("INSERT INTO Categories (name) VALUES (?)", categories)

    # Insert into Businesses table
    businesses = [
        ('Burger King', 'Fast food restaurant', '123 Main St', 'New York', 'NY', '10001', 1),
        ('Walmart', 'Retail store', '456 Broadway', 'Los Angeles', 'CA', '90013', 2),
        ('Hair Salon', 'Beauty services', '789 5th Ave', 'Chicago', 'IL', '60007', 3),
        ('AMC Theatres', 'Movie theater', '901 Broadway', 'Houston', 'TX', '77002', 4),
        ('Yoga Studio', 'Fitness classes', '234 Main St', 'Phoenix', 'AZ', '85004', 5),
        ('Starbucks', 'Coffee shop', '567 5th Ave', 'Philadelphia', 'PA', '19106', 1),
        ('Target', 'Retail store', '890 Broadway', 'San Antonio', 'TX', '78205', 2),
        ('Spa Day', 'Relaxation services', '345 Main St', 'San Diego', 'CA', '92101', 3),
        ('Regal Cinemas', 'Movie theater', '678 Broadway', 'Dallas', 'TX', '75202', 4),
        ('Gym', 'Fitness center', '123 5th Ave', 'San Jose', 'CA', '95101', 5),
    ]
    cur.executemany("""
        INSERT INTO Businesses (name, description, address, city, state, zip, category_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, businesses)

    # Insert into Users table
    users = [
        ('john_doe', 'password123', 'john@example.com'),
        ('jane_doe', 'password123', 'jane@example.com'),
        ('bob_smith', 'password123', 'bob@example.com'),
        ('alice_johnson', 'password123', 'alice@example.com'),
        ('mike_brown', 'password123', 'mike@example.com'),
        ('emily_davis', 'password123', 'emily@example.com'),
        ('david_miller', 'password123', 'david@example.com'),
        ('sarah_taylor', 'password123', 'sarah@example.com'),
        ('kevin_white', 'password123', 'kevin@example.com'),
        ('olivia_martin', 'password123', 'olivia@example.com'),
    ]
    cur.executemany("INSERT INTO Users (username, password, email) VALUES (?, ?, ?)", users)

    # Insert into Reviews table
    reviews = [
        (1, 1, 5, 'Great food and service!',),
        (1, 2, 4, 'Good food, but slow service.',),
        (2, 3, 3, 'Average shopping experience.',),
        (3, 4, 5, 'Excellent hair stylist!',),
        (4, 5, 4, 'Good movie selection, but expensive snacks.',),
        (5, 6, 5, 'Great yoga instructor!',),
        (6, 7, 4, 'Good coffee, but long lines.',),
        (7, 8, 3, 'Average shopping experience.',),
        (8, 9, 5, 'Excellent spa services!',),
        (9, 10, 4, 'Good movie selection, but uncomfortable seats.',),
    ]
    cur.executemany("""
        INSERT INTO Reviews (business_id, user_id, rating, text)
        VALUES (?, ?, ?, ?)
    """, reviews)

    # Commit the changes
    conn.commit()

def main():
    database = 'seed_data.db'

    # Create a connection to the database
    conn = create_connection(database)

    with conn:
        print("Connected to SQLite Database")
        create_seed_data(conn)

if __name__ == '__main__':
    main()