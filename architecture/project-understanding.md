## Project Understanding Document
### 1. Project Summary
The Local Business Discovery App is a web application designed to connect users with local businesses in their area. The primary goal of the system is to provide an intuitive and user-friendly interface for users to discover, explore, and engage with local businesses, while promoting the trend of shopping local and supporting small businesses. The application allows users to view business listings, write reviews, and interact with other users.

### 2. Key Technical Decisions
The following technical decisions were made:
* **Backend:** Python and FastAPI were chosen for building the RESTful API due to their ease of use, scalability, and flexibility.
* **Frontend:** Vanilla HTML/CSS/JS were chosen for building the single-page application due to their lightweight and flexible framework.
* **Database:** SQLite was chosen for storing business listings, user reviews, and ratings due to its ease of use and suitability for small to medium-sized applications.
* **Map Services:** Google Maps API was chosen for providing map-based discovery and location services due to its accuracy and widespread use.

### 3. Critical Data Flows
The following are the 3-5 most important data flows:
* **User Authentication:** The user provides their username and password to obtain a JWT Bearer token, which is then used to authenticate subsequent requests.
* **Business Listings:** The application retrieves business listings from the database and displays them to the user.
* **Review Submission:** The user submits a review, which is then stored in the database and associated with the corresponding business.
* **Business Details:** The application retrieves detailed information about a specific business, including its description, address, and reviews.
* **Map-based Discovery:** The application uses the Google Maps API to provide map-based discovery and location services, allowing users to find businesses near their location.

### 4. API Highlights
The following are the most important endpoints and their purpose:
* **POST /api/v1/auth/login:** Logs in a user and returns a JWT Bearer token.
* **GET /api/v1/businesses:** Returns a list of all businesses.
* **GET /api/v1/businesses/{id}:** Returns a single business by ID.
* **POST /api/v1/reviews:** Submits a review for a business.
* **GET /api/v1/reviews:** Returns a list of reviews for a business.

### 5. Database Relationships
The following are the key table relationships and their business meaning:
* **Users:** A user can write many reviews (one-to-many).
* **Businesses:** A business can have many reviews (one-to-many).
* **Reviews:** A review is written by one user and is for one business (many-to-one).
* **Categories:** A business belongs to one category (many-to-one).

### 6. Security Highlights
The following are the most important security measures:
* **Authentication:** The application uses a JWT Bearer token for authentication.
* **Authorization:** The application uses a Role-Based Access Control (RBAC) system to authorize access to endpoints.
* **Input Validation:** The application validates all user input to prevent SQL injection and cross-site scripting (XSS) attacks.
* **Token Expiry:** The JWT Bearer token expires after 1 hour and can be refreshed by calling the `/auth/refresh` endpoint.

### 7. Integration Points
The following are the integration points between the frontend, backend, and database:
* **Frontend to Backend:** The frontend communicates with the backend using RESTful API calls.
* **Backend to Database:** The backend communicates with the database using SQLite queries.
* **Backend to Google Maps API:** The backend communicates with the Google Maps API using RESTful API calls.

### 8. Audit Checklist
The following is the audit checklist for Phase 3:
* **Authentication:** Verify that the JWT Bearer token is being used correctly for authentication.
* **Authorization:** Verify that the RBAC system is correctly authorizing access to endpoints.
* **Input Validation:** Verify that all user input is being validated correctly to prevent SQL injection and XSS attacks.
* **Database Relationships:** Verify that the database relationships are correctly implemented and functioning as expected.
* **API Endpoints:** Verify that all API endpoints are functioning correctly and returning the expected results.
* **Security Measures:** Verify that all security measures are in place and functioning correctly, including authentication, authorization, and input validation.
* **Error Handling:** Verify that error handling is correctly implemented and functioning as expected.
* **Performance:** Verify that the application is performing well and meeting the required performance standards.