# README-database.md
## Database Overview
The database is designed to store information about businesses, their categories, users, and reviews. It provides a foundation for a business review platform, allowing users to create accounts, leave reviews for businesses, and browse businesses by category.

## Schema Description
The database consists of four tables: `Categories`, `Businesses`, `Users`, and `Reviews`.

### Tables

*   **Categories**: stores unique categories for businesses
    *   `id` (INTEGER PRIMARY KEY AUTOINCREMENT): unique identifier for the category
    *   `name` (TEXT NOT NULL UNIQUE): name of the category
*   **Businesses**: stores information about businesses
    *   `id` (INTEGER PRIMARY KEY AUTOINCREMENT): unique identifier for the business
    *   `name` (TEXT NOT NULL): name of the business
    *   `description` (TEXT NOT NULL): description of the business
    *   `address` (TEXT NOT NULL): address of the business
    *   `city` (TEXT NOT NULL): city of the business
    *   `state` (TEXT NOT NULL): state of the business
    *   `zip` (TEXT NOT NULL): zip code of the business
    *   `category_id` (INTEGER NOT NULL): foreign key referencing the `id` in `Categories`
*   **Users**: stores information about users
    *   `id` (INTEGER PRIMARY KEY AUTOINCREMENT): unique identifier for the user
    *   `username` (TEXT NOT NULL UNIQUE): username chosen by the user
    *   `password` (TEXT NOT NULL): password for the user's account
    *   `email` (TEXT NOT NULL UNIQUE): email address of the user
*   **Reviews**: stores reviews left by users for businesses
    *   `id` (INTEGER PRIMARY KEY AUTOINCREMENT): unique identifier for the review
    *   `business_id` (INTEGER NOT NULL): foreign key referencing the `id` in `Businesses`
    *   `user_id` (INTEGER NOT NULL): foreign key referencing the `id` in `Users`
    *   `rating` (INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5)): rating given by the user (between 1 and 5)
    *   `text` (TEXT NOT NULL): text of the review
    *   `created_at` (DATETIME DEFAULT CURRENT_TIMESTAMP): timestamp when the review was created

### Relationships

*   A category can have multiple businesses (one-to-many).
*   A business belongs to one category (many-to-one).
*   A user can leave multiple reviews (one-to-many).
*   A review is left by one user (many-to-one).
*   A business can have multiple reviews (one-to-many).
*   A review is for one business (many-to-one).

## Setup Instructions
To set up the database, follow these steps:

1.  Install a compatible database management system (e.g., SQLite).
2.  Create a new database.
3.  Execute the provided SQL script to create the tables and indexes.

## How to Run Migrations
Since this is a simple database setup, migrations are not necessary. However, if you need to make changes to the schema in the future, you can create migration scripts to apply those changes.

## How to Seed Data
To seed the database with initial data, you can insert records into the tables manually or create a script to automate the process. For example:

```sql
INSERT INTO Categories (name) VALUES ('Restaurant');
INSERT INTO Categories (name) VALUES ('Shop');

INSERT INTO Businesses (name, description, address, city, state, zip, category_id)
VALUES ('Example Restaurant', 'A great place to eat', '123 Main St', 'Anytown', 'CA', '12345', 1);

INSERT INTO Users (username, password, email)
VALUES ('john_doe', 'password123', 'john@example.com');

INSERT INTO Reviews (business_id, user_id, rating, text)
VALUES (1, 1, 5, 'Great food and service!');
```

## Query Examples
Here are some example queries to demonstrate how to retrieve data from the database:

```sql
-- Get all businesses in a specific category
SELECT * FROM Businesses WHERE category_id = 1;

-- Get all reviews for a specific business
SELECT * FROM Reviews WHERE business_id = 1;

-- Get the average rating for a specific business
SELECT AVG(rating) FROM Reviews WHERE business_id = 1;

-- Get all businesses with their corresponding categories
SELECT b.*, c.name AS category_name
FROM Businesses b
JOIN Categories c ON b.category_id = c.id;
```

## Index Optimization Notes
Indexes have been created on the following columns to improve query performance:

*   `Businesses.name`
*   `Reviews.business_id`
*   `Reviews.user_id`

These indexes can be adjusted or additional indexes can be created based on the specific query patterns and performance requirements of your application.

## Backup Strategy
To ensure data integrity and availability, it's essential to implement a regular backup strategy for your database. This can include:

*   Daily full backups
*   Hourly incremental backups
*   Weekly or monthly partial backups (e.g., backing up only specific tables or data)

You can use database management system tools or third-party backup software to automate the backup process and store backups securely.