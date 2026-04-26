import jwt
from datetime import datetime, timedelta
from typing import Dict

def create_jwt_token(user_id: int, username: str, email: str, secret_key: str) -> str:
    """
    Creates a JWT token for the given user.
    
    Args:
    user_id (int): The ID of the user.
    username (str): The username of the user.
    email (str): The email of the user.
    secret_key (str): The secret key used to sign the token.
    
    Returns:
    str: The JWT token.
    """
    payload: Dict[str, str] = {
        'user_id': str(user_id),
        'username': username,
        'email': email,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, secret_key, algorithm='HS256')

def verify_jwt_token(token: str, secret_key: str) -> Dict[str, str]:
    """
    Verifies the given JWT token.
    
    Args:
    token (str): The JWT token to verify.
    secret_key (str): The secret key used to sign the token.
    
    Returns:
    Dict[str, str]: The payload of the token if it is valid, otherwise None.
    """
    try:
        return jwt.decode(token, secret_key, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None