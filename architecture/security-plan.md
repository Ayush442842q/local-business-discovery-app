# Security Plan for Local Business Discovery App
## Introduction
The Local Business Discovery App is a web application designed to connect users with local businesses in their area. As with any web application, security is a top priority to ensure the protection of user data and prevent unauthorized access. This security plan outlines the measures that will be taken to ensure the security of the application.

## Authentication Strategy
The application will use a JSON Web Token (JWT) based authentication system. The token will be obtained by calling the `/auth/login` endpoint and will be required for all subsequent requests.

* **Token Structure:** The token will contain the user's ID, username, and email.
* **Token Expiry:** The token will expire after 1 hour.
* **Token Refresh:** The token can be refreshed by calling the `/auth/refresh` endpoint.
* **Token Validation:** The token will be validated on each request to ensure it has not expired and is valid.

## Authorization
The application will use a Role-Based Access Control (RBAC) system to authorize access to endpoints.

* **Roles:** The application will have the following roles:
	+ **Admin:** Can access all endpoints.
	+ **User:** Can access endpoints related to user functionality (e.g. viewing businesses, writing reviews).
* **Endpoint Access:** The following endpoints will be restricted to specific roles:
	+ **GET /api/v1/businesses:** Admin, User
	+ **GET /api/v1/businesses/{id}:** Admin, User
	+ **POST /api/v1/reviews:** User
	+ **GET /api/v1/reviews:** Admin, User

## Input Validation
The application will validate all user input to prevent SQL injection and cross-site scripting (XSS) attacks.

* **Validation Rules:**
	+ **Username:** Must be between 3 and 20 characters long, can only contain letters, numbers, and underscores.
	+ **Password:** Must be between 8 and 20 characters long, must contain at least one uppercase letter, one lowercase letter, and one number.
	+ **Email:** Must be a valid email address.
	+ **Business Name:** Must be between 3 and 50 characters long, can only contain letters, numbers, and spaces.
	+ **Business Description:** Must be between 10 and 200 characters long, can only contain letters, numbers, and spaces.
	+ **Review Text:** Must be between 10 and 200 characters long, can only contain letters, numbers, and spaces.

## Password Security
The application will store passwords securely using a hashing algorithm.

* **Hashing Algorithm:** The application will use the bcrypt hashing algorithm.
* **Salt:** A random salt will be generated for each user and stored along with the hashed password.
* **Password Storage:** The hashed password and salt will be stored in the database.

## CORS Configuration
The application will be configured to only allow requests from specific origins.

* **Allowed Origins:** The application will only allow requests from the following origins:
	+ **https://localbusinessdiscovery.app**
	+ **https://api.localbusinessdiscovery.app**
* **Allowed Methods:** The application will only allow the following methods:
	+ **GET**
	+ **POST**
	+ **PUT**
	+ **DELETE**
* **Allowed Headers:** The application will only allow the following headers:
	+ **Content-Type**
	+ **Authorization**

## Rate Limiting
The application will be configured to limit the number of requests from a single IP address.

* **Limit:** The application will limit requests to 100 per minute per IP address.
* **Exceeding Limit:** If a user exceeds the limit, they will receive a 429 error response.

## SQL Injection Prevention
The application will use parameterized queries to prevent SQL injection attacks.

* **Parameterized Queries:** The application will use parameterized queries to prevent user input from being executed as SQL code.
* **ORM:** The application will use an Object-Relational Mapping (ORM) tool to interact with the database and prevent SQL injection attacks.

## Sensitive Data
The application will not store sensitive data such as credit card numbers or social security numbers.

* **What Not to Store:** The application will not store the following sensitive data:
	+ **Credit Card Numbers**
	+ **Social Security Numbers**
	+ **Driver's License Numbers**
* **What to Encrypt:** The application will encrypt the following data:
	+ **Passwords**
	+ **Email Addresses**
* **Environment Variables:** The application will use environment variables to store sensitive data such as API keys and database credentials.

## HTTPS & Headers
The application will use HTTPS to encrypt data in transit and will include security headers in responses.

* **Security Headers:** The application will include the following security headers in responses:
	+ **Content-Security-Policy (CSP):** Will define which sources of content are allowed to be executed within a web page.
	+ **HTTP Strict Transport Security (HSTS):** Will instruct the browser to only use HTTPS to communicate with the application.
	+ **X-Frame-Options:** Will prevent the application from being framed by another website.

## Error Handling
The application will handle errors securely to prevent information disclosure.

* **Error Handling:** The application will handle errors by logging the error and returning a generic error message to the user.
* **Error Response:** The application will return a generic error response with a 500 status code.
* **Error Logging:** The application will log errors to a secure logging system for further investigation.