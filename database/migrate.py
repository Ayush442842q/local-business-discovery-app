import sqlite3
from sqlite3 import Error

class DatabaseMigration:
    def __init__(self, db_name):
        self.conn = None
        self.db_name = db_name
        self.migration_table = 'Migrations'

    def create_connection(self):
        """Create a connection to the SQLite database"""
        try:
            self.conn = sqlite3.connect(self.db_name)
            print(f"Connected to {self.db_name} database")
        except Error as e:
            print(e)

    def create_migration_table(self):
        """Create migration tracking table if it doesn't exist"""
        query = f"""
            CREATE TABLE IF NOT EXISTS {self.migration_table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                applied_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """
        try:
            self.conn.execute(query)
            print(f"Created {self.migration_table} table")
        except Error as e:
            print(e)

    def apply_migration(self, migration_name, query):
        """Apply a migration if it hasn't been applied before"""
        try:
            self.conn.execute(query)
            self.conn.execute(f"""
                INSERT INTO {self.migration_table} (name) VALUES (?)
            """, (migration_name,))
            self.conn.commit()
            print(f"Applied migration: {migration_name}")
        except Error as e:
            print(e)

    def rollback_migration(self, migration_name):
        """Rollback a migration if it has been applied before"""
        try:
            self.conn.execute(f"""
                DELETE FROM {self.migration_table} WHERE name = ?
            """, (migration_name,))
            self.conn.commit()
            print(f"Rolled back migration: {migration_name}")
        except Error as e:
            print(e)

    def has_migration_been_applied(self, migration_name):
        """Check if a migration has been applied before"""
        query = f"""
            SELECT * FROM {self.migration_table} WHERE name = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (migration_name,))
        return cursor.fetchone() is not None

    def create_categories_table(self):
        """Create Categories table if it doesn't exist"""
        migration_name = 'create_categories_table'
        query = """
            CREATE TABLE IF NOT EXISTS Categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """
        if not self.has_migration_been_applied(migration_name):
            self.apply_migration(migration_name, query)

    def create_businesses_table(self):
        """Create Businesses table if it doesn't exist"""
        migration_name = 'create_businesses_table'
        query = """
            CREATE TABLE IF NOT EXISTS Businesses (
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
            )
        """
        if not self.has_migration_been_applied(migration_name):
            self.apply_migration(migration_name, query)

    def create_users_table(self):
        """Create Users table if it doesn't exist"""
        migration_name = 'create_users_table'
        query = """
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """
        if not self.has_migration_been_applied(migration_name):
            self.apply_migration(migration_name, query)

    def create_reviews_table(self):
        """Create Reviews table if it doesn't exist"""
        migration_name = 'create_reviews_table'
        query = """
            CREATE TABLE IF NOT EXISTS Reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                business_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
                text TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (business_id) REFERENCES Businesses (id) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE ON UPDATE CASCADE
            )
        """
        if not self.has_migration_been_applied(migration_name):
            self.apply_migration(migration_name, query)

    def create_indexes(self):
        """Create indexes for faster querying"""
        migration_name = 'create_indexes'
        queries = [
            """
                CREATE INDEX IF NOT EXISTS idx_businesses_name ON Businesses (name)
            """,
            """
                CREATE INDEX IF NOT EXISTS idx_reviews_business_id ON Reviews (business_id)
            """,
            """
                CREATE INDEX IF NOT EXISTS idx_reviews_user_id ON Reviews (user_id)
            """
        ]
        if not self.has_migration_been_applied(migration_name):
            for query in queries:
                self.apply_migration(migration_name, query)

    def migrate(self):
        """Apply all migrations"""
        self.create_migration_table()
        self.create_categories_table()
        self.create_businesses_table()
        self.create_users_table()
        self.create_reviews_table()
        self.create_indexes()

    def close_connection(self):
        """Close the connection to the SQLite database"""
        if self.conn:
            self.conn.close()
            print("Connection closed")


def main():
    db_name = 'example.db'
    migration = DatabaseMigration(db_name)
    migration.create_connection()
    migration.migrate()
    migration.close_connection()


if __name__ == '__main__':
    main()