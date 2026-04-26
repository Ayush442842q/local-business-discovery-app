# models.py
from typing import Dict
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# Association table for many-to-many relationship between Business and Category
business_category_table = Table(
    'business_category',
    Base.metadata,
    Column('business_id', Integer, ForeignKey('businesses.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

class Category(Base):
    """Category model"""
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    businesses = relationship('Business', secondary=business_category_table, back_populates='categories')

    def __init__(self, name: str):
        self.name = name

    def to_dict(self) -> Dict:
        """Serialize Category model to dictionary"""
        return {
            'id': self.id,
            'name': self.name
        }

class Business(Base):
    """Business model"""
    __tablename__ = 'businesses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip = Column(String, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    categories = relationship('Category', secondary=business_category_table, back_populates='businesses')
    reviews = relationship('Review', back_populates='business')

    def __init__(self, name: str, description: str, address: str, city: str, state: str, zip: str, latitude: float = None, longitude: float = None):
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.latitude = latitude
        self.longitude = longitude

    def to_dict(self) -> Dict:
        """Serialize Business model to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip': self.zip,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

class User(Base):
    """User model"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    reviews = relationship('Review', back_populates='user')

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def to_dict(self) -> Dict:
        """Serialize User model to dictionary"""
        return {
            'id': self.id,
            'username': self.username
        }

class Review(Base):
    """Review model"""
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    business_id = Column(Integer, ForeignKey('businesses.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    business = relationship('Business', back_populates='reviews')
    user = relationship('User', back_populates='reviews')

    def __init__(self, business_id: int, user_id: int, rating: int, text: str):
        self.business_id = business_id
        self.user_id = user_id
        self.rating = rating
        self.text = text

    def to_dict(self) -> Dict:
        """Serialize Review model to dictionary"""
        return {
            'id': self.id,
            'business_id': self.business_id,
            'user_id': self.user_id,
            'rating': self.rating,
            'text': self.text,
            'created_at': self.created_at
        }