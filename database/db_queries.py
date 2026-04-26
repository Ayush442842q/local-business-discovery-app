import sqlite3
from sqlite3 import Error

class DatabaseQueries:
    def __init__(self, db_file):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)

    def create_table_categories(self):
        query = """CREATE TABLE IF NOT EXISTS Categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                )"""
        try:
            self.conn.execute(query)
            print("Categories table created successfully")
        except Error as e:
            print(e)

    def create_table_businesses(self):
        query = """CREATE TABLE IF NOT EXISTS Businesses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    address TEXT NOT NULL,
                    city TEXT NOT NULL,
                    state TEXT NOT NULL,
                    zip TEXT NOT NULL,
                    category_id INTEGER NOT NULL,
                    FOREIGN KEY (category_id) REFERENCES Categories (id) ON DELETE CASCADE ON UPDATE CASCADE,
                    UNIQUE (name, address)
                )"""
        try:
            self.conn.execute(query)
            print("Businesses table created successfully")
        except Error as e:
            print(e)

    def create_table_users(self):
        query = """CREATE TABLE IF NOT EXISTS Users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                )"""
        try:
            self.conn.execute(query)
            print("Users table created successfully")
        except Error as e:
            print(e)

    def create_table_reviews(self):
        query = """CREATE TABLE IF NOT EXISTS Reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    business_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
                    text TEXT NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (business_id) REFERENCES Businesses (id) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE ON UPDATE CASCADE
                )"""
        try:
            self.conn.execute(query)
            print("Reviews table created successfully")
        except Error as e:
            print(e)

    def create_index_businesses_name(self):
        query = """CREATE INDEX IF NOT EXISTS idx_businesses_name ON Businesses (name)"""
        try:
            self.conn.execute(query)
            print("Index on Businesses name created successfully")
        except Error as e:
            print(e)

    def create_index_reviews_business_id(self):
        query = """CREATE INDEX IF NOT EXISTS idx_reviews_business_id ON Reviews (business_id)"""
        try:
            self.conn.execute(query)
            print("Index on Reviews business_id created successfully")
        except Error as e:
            print(e)

    def create_index_reviews_user_id(self):
        query = """CREATE INDEX IF NOT EXISTS idx_reviews_user_id ON Reviews (user_id)"""
        try:
            self.conn.execute(query)
            print("Index on Reviews user_id created successfully")
        except Error as e:
            print(e)

    # CRUD operations for Categories
    def create_category(self, name):
        query = """INSERT INTO Categories (name) VALUES (?)"""
        try:
            self.conn.execute(query, (name,))
            self.conn.commit()
            return True
        except Error as e:
            print(e)
            return False

    def read_category(self, id):
        query = """SELECT * FROM Categories WHERE id = ?"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (id,))
            return cursor.fetchone()
        except Error as e:
            print(e)
            return None

    def update_category(self, id, name):
        query = """UPDATE Categories SET name = ? WHERE id = ?"""
        try:
            self.conn.execute(query, (name, id))
            self.conn.commit()
            return True
        except Error as e:
            print(e)
            return False

    def delete_category(self, id):
        query = """DELETE FROM Categories WHERE id = ?"""
        try:
            self.conn.execute(query, (id,))
            self.conn.commit()
            return True
        except Error as e:
            print(e)
            return False

    # CRUD operations for Businesses
    def create_business(self, name, description, address, city, state, zip, category_id):
        query = """INSERT INTO Businesses (name, description, address, city, state, zip, category_id) VALUES (?, ?, ?, ?, ?, ?, ?)"""
        try:
            self.conn.execute(query, (name, description, address, city, state, zip, category_id))
            self.conn.commit()
            return True
        except Error as e:
            print(e)
            return False

    def read_business(self, id):
        query = """SELECT * FROM Businesses WHERE id = ?"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (id,))
            return cursor.fetchone()
        except Error as e:
            print(e)
            return None

    def update_business(self, id, name, description, address, city, state, zip, category_id):
        query = """UPDATE Businesses SET name = ?, description = ?, address = ?, city = ?, state = ?, zip = ?, category_id = ? WHERE id = ?"""
        try:
            self.conn.execute(query, (name, description, address, city, state, zip, category_id, id))
            self.conn.commit()
            return True
        except Error as e:
            print(e)
            return False

    def delete_business(self, id):
        query = """DELETE FROM Businesses WHERE id = ?"""
        try:
            self.conn.execute(query, (id,))
            self.conn.commit()
            return True
        except Error as e:
            print(e)
            return False

    # CRUD operations for Users
    def create_user(self, username, password, email):
        query = """INSERT INTO Users (username, password, email) VALUES (?, ?, ?)"""
        try:
            self.conn.execute(query, (username, password, email))
            self.conn.commit()
            return True
        except Error as e:
            print(e)
            return False

    def read_user(self, id):
        query = """SELECT * FROM Users WHERE id = ?"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (id,))
            return cursor.fetchone()
        except Error as e:
            print(e)
            return None

    def update_user(self, id, username, password, email):
        query = """UPDATE Users SET username = ?, password = ?, email = ? WHERE id = ?"""
        try:
            self.conn.execute(query, (username, password, email, id))
            self.conn.commit()
            return True
        except Error as e:
            print(e)
            return False

    def delete_user(self, id):
        query = """DELETE FROM Users WHERE id = ?"""
        try:
            self.conn.execute(query, (id,))
            self.conn.commit()
            return True
        except Error as e:
            print(e)
            return False

    # CRUD operations for Reviews
    def create_review(self, business_id, user_id, rating, text):
        query = """INSERT INTO Reviews (business_id, user_id, rating, text) VALUES (?, ?, ?, ?)"""
        try:
            self.conn.execute(query, (business_id, user_id, rating, text))
            self.conn.commit()
            return True
        except Error as e:
            print(e)
            return False

    def read_review(self, id):
        query = """SELECT * FROM Reviews WHERE id = ?"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (id,))
            return cursor.fetchone()
        except Error as e:
            print(e)
            return None

    def update_review(self, id, business_id, user_id, rating, text):
        query = """UPDATE Reviews SET business_id = ?, user_id = ?, rating = ?, text = ? WHERE id = ?"""
        try:
            self.conn.execute(query, (business_id, user_id, rating, text, id))
            self.conn.commit()
            return True
        except Error as e:
            print(e)
            return False

    def delete_review(self, id):
        query = """DELETE FROM Reviews WHERE id = ?"""
        try:
            self.conn.execute(query, (id,))
            self.conn.commit()
            return True
        except Error as e:
            print(e)
            return False

    # Join queries
    def get_businesses_with_categories(self):
        query = """SELECT B.id, B.name, B.description, B.address, B.city, B.state, B.zip, C.name AS category_name
                   FROM Businesses B
                   JOIN Categories C ON B.category_id = C.id"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(e)
            return None

    def get_reviews_with_businesses_and_users(self):
        query = """SELECT R.id, R.business_id, R.user_id, R.rating, R.text, B.name AS business_name, U.username AS user_username
                   FROM Reviews R
                   JOIN Businesses B ON R.business_id = B.id
                   JOIN Users U ON R.user_id = U.id"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(e)
            return None

    # Search/filter queries
    def search_businesses_by_name(self, name):
        query = """SELECT * FROM Businesses WHERE name LIKE ?"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, ('%' + name + '%',))
            return cursor.fetchall()
        except Error as e:
            print(e)
            return None

    def search_reviews_by_text(self, text):
        query = """SELECT * FROM Reviews WHERE text LIKE ?"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, ('%' + text + '%',))
            return cursor.fetchall()
        except Error as e:
            print(e)
            return None

    # Pagination support
    def get_businesses_with_pagination(self, limit, offset):
        query = """SELECT * FROM Businesses LIMIT ? OFFSET ?"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (limit, offset))
            return cursor.fetchall()
        except Error as e:
            print(e)
            return None

    def get_reviews_with_pagination(self, limit, offset):
        query = """SELECT * FROM Reviews LIMIT ? OFFSET ?"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (limit, offset))
            return cursor.fetchall()
        except Error as e:
            print(e)
            return None

# Example usage
db = DatabaseQueries('database.db')
db.create_table_categories()
db.create_table_businesses()
db.create_table_users()
db.create_table_reviews()
db.create_index_businesses_name()
db.create_index_reviews_business_id()
db.create_index_reviews_user_id()

# Create a new category
db.create_category('Food')

# Create a new business
db.create_business('Restaurant', 'A great restaurant', '123 Main St', 'Anytown', 'CA', '12345', 1)

# Create a new user
db.create_user('user123', 'pass123', 'user123@example.com')

# Create a new review
db.create_review(1, 1, 5, 'This is a great restaurant!')

# Get all businesses with categories
businesses = db.get_businesses_with_categories()
for business in businesses:
    print(business)

# Get all reviews with businesses and users
reviews = db.get_reviews_with_businesses_and_users()
for review in reviews:
    print(review)

# Search for businesses by name
search_results = db.search_businesses_by_name('Restaurant')
for result in search_results:
    print(result)

# Get businesses with pagination
paginated_results = db.get_businesses_with_pagination(10, 0)
for result in paginated_results:
    print(result)