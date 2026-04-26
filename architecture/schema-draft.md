# Database Schema for Local Business Discovery App
## Entity Overview
The following entities will be used in the database schema:
* **Users**: represents a user of the application
* **Businesses**: represents a business listed in the application
* **Reviews**: represents a review written by a user for a business
* **Categories**: represents a category that a business can belong to

## Schema Tables
### Users Table
| Column Name | Data Type | Constraints |
| --- | --- | --- |
| id | INTEGER | PRIMARY KEY, UNIQUE, NOT NULL |
| username | TEXT | NOT NULL, UNIQUE |
| password | TEXT | NOT NULL |
| email | TEXT | NOT NULL, UNIQUE |

### Businesses Table
| Column Name | Data Type | Constraints |
| --- | --- | --- |
| id | INTEGER | PRIMARY KEY, UNIQUE, NOT NULL |
| name | TEXT | NOT NULL |
| description | TEXT | NOT NULL |
| address | TEXT | NOT NULL |
| city | TEXT | NOT NULL |
| state | TEXT | NOT NULL |
| zip | TEXT | NOT NULL |
| category_id | INTEGER | FOREIGN KEY REFERENCES Categories(id) |

### Reviews Table
| Column Name | Data Type | Constraints |
| --- | --- | --- |
| id | INTEGER | PRIMARY KEY, UNIQUE, NOT NULL |
| business_id | INTEGER | FOREIGN KEY REFERENCES Businesses(id) |
| user_id | INTEGER | FOREIGN KEY REFERENCES Users(id) |
| rating | INTEGER | NOT NULL |
| text | TEXT | NOT NULL |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP |

### Categories Table
| Column Name | Data Type | Constraints |
| --- | --- | --- |
| id | INTEGER | PRIMARY KEY, UNIQUE, NOT NULL |
| name | TEXT | NOT NULL, UNIQUE |

### Indexes
* CREATE INDEX idx_businesses_name ON Businesses (name)
* CREATE INDEX idx_reviews_business_id ON Reviews (business_id)
* CREATE INDEX idx_reviews_user_id ON Reviews (user_id)

## Relationships
The relationships between the entities are as follows:
* A user can write many reviews (one-to-many).
* A business can have many reviews (one-to-many).
* A review is written by one user and is for one business (many-to-one).
* A business belongs to one category (many-to-one).

ER diagram in text format:
```
+---------------+
|     Users     |
+---------------+
       |
       | 1:N
       v
+---------------+
|     Reviews   |
+---------------+
       |
       | 1:N
       v
+---------------+
|   Businesses  |
+---------------+
       |
       | 1:1
       v
+---------------+
|   Categories  |
+---------------+
```

## Sample Queries
1. Get all businesses in a specific category:
```sql
SELECT * FROM Businesses WHERE category_id = 1;
```
2. Get all reviews for a specific business:
```sql
SELECT * FROM Reviews WHERE business_id = 1;
```
3. Get the average rating for a specific business:
```sql
SELECT AVG(rating) FROM Reviews WHERE business_id = 1;
```
4. Get all businesses with a rating above 4:
```sql
SELECT b.* FROM Businesses b JOIN Reviews r ON b.id = r.business_id GROUP BY b.id HAVING AVG(r.rating) > 4;
```
5. Get the top 10 businesses with the most reviews:
```sql
SELECT b.* FROM Businesses b JOIN Reviews r ON b.id = r.business_id GROUP BY b.id ORDER BY COUNT(r.id) DESC LIMIT 10;
```

## Migration Notes
To create the tables in the correct order, follow these steps:
1. Create the Categories table.
2. Create the Businesses table.
3. Create the Users table.
4. Create the Reviews table.
This order ensures that the foreign key constraints are satisfied.