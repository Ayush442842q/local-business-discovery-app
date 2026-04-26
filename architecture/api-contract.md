# Local Business Discovery App API Contract
## Base URL and Versioning Strategy
The base URL for the API is `https://api.localbusinessdiscovery.app/v1`. The API uses a versioning strategy based on the URL path, with the version number included in the path.

## Authentication Scheme
The API uses a JWT Bearer token for authentication. The token is obtained by calling the `/auth/login` endpoint and is required for all subsequent requests.

## Global Error Format
The API returns errors in the following format:
```json
{
  "error": {
    "code": 400,
    "message": "Invalid request"
  }
}
```
## Rate Limiting Policy
The API has a rate limiting policy of 100 requests per minute per IP address. Exceeding this limit will result in a 429 error response.

## Endpoints

### 1. POST /api/v1/auth/login
#### Description
Logs in a user and returns a JWT Bearer token.
#### Authentication
None
#### Request Body
```json
{
  "username": "string",
  "password": "string"
}
```
#### Success Response
```json
{
  "token": "string"
}
```
#### Error Responses
* 401: Invalid username or password
* 500: Internal server error
#### Example Request/Response Pair
```bash
curl -X POST \
  https://api.localbusinessdiscovery.app/v1/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"username": "user123", "password": "pass123"}'
```
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
```

### 2. GET /api/v1/businesses
#### Description
Returns a list of all businesses.
#### Authentication
Required (JWT Bearer token)
#### Request Body
None
#### Success Response
```json
[
  {
    "id": 1,
    "name": "Business 1",
    "description": "This is business 1",
    "address": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345"
  },
  {
    "id": 2,
    "name": "Business 2",
    "description": "This is business 2",
    "address": "456 Elm St",
    "city": "Othertown",
    "state": "NY",
    "zip": "67890"
  }
]
```
#### Error Responses
* 401: Unauthorized
* 500: Internal server error
#### Example Request/Response Pair
```bash
curl -X GET \
  https://api.localbusinessdiscovery.app/v1/businesses \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
```
```json
[
  {
    "id": 1,
    "name": "Business 1",
    "description": "This is business 1",
    "address": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345"
  },
  {
    "id": 2,
    "name": "Business 2",
    "description": "This is business 2",
    "address": "456 Elm St",
    "city": "Othertown",
    "state": "NY",
    "zip": "67890"
  }
]
```

### 3. GET /api/v1/businesses/{id}
#### Description
Returns a single business by ID.
#### Authentication
Required (JWT Bearer token)
#### Request Body
None
#### Success Response
```json
{
  "id": 1,
  "name": "Business 1",
  "description": "This is business 1",
  "address": "123 Main St",
  "city": "Anytown",
  "state": "CA",
  "zip": "12345"
}
```
#### Error Responses
* 401: Unauthorized
* 404: Business not found
* 500: Internal server error
#### Example Request/Response Pair
```bash
curl -X GET \
  https://api.localbusinessdiscovery.app/v1/businesses/1 \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
```
```json
{
  "id": 1,
  "name": "Business 1",
  "description": "This is business 1",
  "address": "123 Main St",
  "city": "Anytown",
  "state": "CA",
  "zip": "12345"
}
```

### 4. POST /api/v1/reviews
#### Description
Creates a new review for a business.
#### Authentication
Required (JWT Bearer token)
#### Request Body
```json
{
  "business_id": 1,
  "rating": 5,
  "text": "This is a great business!"
}
```
#### Success Response
```json
{
  "id": 1,
  "business_id": 1,
  "rating": 5,
  "text": "This is a great business!"
}
```
#### Error Responses
* 401: Unauthorized
* 400: Invalid request
* 500: Internal server error
#### Example Request/Response Pair
```bash
curl -X POST \
  https://api.localbusinessdiscovery.app/v1/reviews \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
  -H 'Content-Type: application/json' \
  -d '{"business_id": 1, "rating": 5, "text": "This is a great business!"}'
```
```json
{
  "id": 1,
  "business_id": 1,
  "rating": 5,
  "text": "This is a great business!"
}
```

### 5. GET /api/v1/reviews
#### Description
Returns a list of all reviews.
#### Authentication
Required (JWT Bearer token)
#### Request Body
None
#### Success Response
```json
[
  {
    "id": 1,
    "business_id": 1,
    "rating": 5,
    "text": "This is a great business!"
  },
  {
    "id": 2,
    "business_id": 2,
    "rating": 4,
    "text": "This is a good business!"
  }
]
```
#### Error Responses
* 401: Unauthorized
* 500: Internal server error
#### Example Request/Response Pair
```bash
curl -X GET \
  https://api.localbusinessdiscovery.app/v1/reviews \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
```
```json
[
  {
    "id": 1,
    "business_id": 1,
    "rating": 5,
    "text": "This is a great business!"
  },
  {
    "id": 2,
    "business_id": 2,
    "rating": 4,
    "text": "This is a good business!"
  }
]
```

### 6. GET /api/v1/businesses/nearby
#### Description
Returns a list of nearby businesses based on the user's location.
#### Authentication
Required (JWT Bearer token)
#### Request Body
None
#### Success Response
```json
[
  {
    "id": 1,
    "name": "Business 1",
    "description": "This is business 1",
    "address": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345",
    "distance": 0.5
  },
  {
    "id": 2,
    "name": "Business 2",
    "description": "This is business 2",
    "address": "456 Elm St",
    "city": "Othertown",
    "state": "NY",
    "zip": "67890",
    "distance": 1.2
  }
]
```
#### Error Responses
* 401: Unauthorized
* 500: Internal server error
#### Example Request/Response Pair
```bash
curl -X GET \
  https://api.localbusinessdiscovery.app/v1/businesses/nearby \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
```
```json
[
  {
    "id": 1,
    "name": "Business 1",
    "description": "This is business 1",
    "address": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345",
    "distance": 0.5
  },
  {
    "id": 2,
    "name": "Business 2",
    "description": "This is business 2",
    "address": "456 Elm St",
    "city": "Othertown",
    "state": "NY",
    "zip": "67890",
    "distance": 1.2
  }
]
```

### 7. GET /api/v1/recommendations
#### Description
Returns a list of recommended businesses based on the user's preferences.
#### Authentication
Required (JWT Bearer token)
#### Request Body
None
#### Success Response
```json
[
  {
    "id": 1,
    "name": "Business 1",
    "description": "This is business 1",
    "address": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345"
  },
  {
    "id": 2,
    "name": "Business 2",
    "description": "This is business 2",
    "address": "456 Elm St",
    "city": "Othertown",
    "state": "NY",
    "zip": "67890"
  }
]
```
#### Error Responses
* 401: Unauthorized
* 500: Internal server error
#### Example Request/Response Pair
```bash
curl -X GET \
  https://api.localbusinessdiscovery.app/v1/recommendations \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
```
```json
[
  {
    "id": 1,
    "name": "Business 1",
    "description": "This is business 1",
    "address": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345"
  },
  {
    "id": 2,
    "name": "Business 2",
    "description": "This is business 2",
    "address": "456 Elm St",
    "city": "Othertown",
    "state": "NY",
    "zip": "67890"
  }
]
```