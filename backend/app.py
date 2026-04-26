from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import List
import sqlite3
import jwt
import logging
from logging.handlers import RotatingFileHandler
import os
import uvicorn
from starlette.middleware.cors import CORSMiddleware

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=1)
logger.addHandler(handler)

# Set up database connection
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS businesses (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        zip TEXT NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY,
        business_id INTEGER NOT NULL,
        rating INTEGER NOT NULL,
        text TEXT NOT NULL,
        FOREIGN KEY (business_id) REFERENCES businesses (id)
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Create a FastAPI app
app = FastAPI()

# Set up CORS
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up JWT authentication
security = HTTPBearer()

# Define a function to get the current user
async def get_current_user(token: str = Depends(security)):
    try:
        payload = jwt.decode(token.credentials, os.environ['SECRET_KEY'], algorithms=['HS256'])
        return payload['username']
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Define the models
class Business(BaseModel):
    id: int
    name: str
    description: str
    address: str
    city: str
    state: str
    zip: str

class Review(BaseModel):
    id: int
    business_id: int
    rating: int
    text: str

class User(BaseModel):
    id: int
    username: str
    password: str

# Define the routes
@app.post("/api/v1/auth/login")
async def login(username: str, password: str):
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    if user:
        payload = {'username': username}
        token = jwt.encode(payload, os.environ['SECRET_KEY'], algorithm='HS256')
        return {'token': token}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

@app.get("/api/v1/businesses")
async def get_businesses(current_user: str = Depends(get_current_user)):
    cursor.execute('SELECT * FROM businesses')
    businesses = cursor.fetchall()
    return [Business(id=business[0], name=business[1], description=business[2], address=business[3], city=business[4], state=business[5], zip=business[6]) for business in businesses]

@app.get("/api/v1/businesses/{id}")
async def get_business(id: int, current_user: str = Depends(get_current_user)):
    cursor.execute('SELECT * FROM businesses WHERE id = ?', (id,))
    business = cursor.fetchone()
    if business:
        return Business(id=business[0], name=business[1], description=business[2], address=business[3], city=business[4], state=business[5], zip=business[6])
    else:
        raise HTTPException(status_code=404, detail="Business not found")

@app.post("/api/v1/reviews")
async def create_review(business_id: int, rating: int, text: str, current_user: str = Depends(get_current_user)):
    cursor.execute('INSERT INTO reviews (business_id, rating, text) VALUES (?, ?, ?)', (business_id, rating, text))
    conn.commit()
    return Review(id=cursor.lastrowid, business_id=business_id, rating=rating, text=text)

@app.get("/api/v1/reviews")
async def get_reviews(current_user: str = Depends(get_current_user)):
    cursor.execute('SELECT * FROM reviews')
    reviews = cursor.fetchall()
    return [Review(id=review[0], business_id=review[1], rating=review[2], text=review[3]) for review in reviews]

@app.get("/api/v1/businesses/nearby")
async def get_nearby_businesses(current_user: str = Depends(get_current_user)):
    # This is a placeholder for a more complex implementation
    cursor.execute('SELECT * FROM businesses')
    businesses = cursor.fetchall()
    return [Business(id=business[0], name=business[1], description=business[2], address=business[3], city=business[4], state=business[5], zip=business[6]) for business in businesses]

@app.get("/api/v1/recommendations")
async def get_recommendations(current_user: str = Depends(get_current_user)):
    # This is a placeholder for a more complex implementation
    cursor.execute('SELECT * FROM businesses')
    businesses = cursor.fetchall()
    return [Business(id=business[0], name=business[1], description=business[2], address=business[3], city=business[4], state=business[5], zip=business[6]) for business in businesses]

# Start the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)