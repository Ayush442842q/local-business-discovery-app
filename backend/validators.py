import re
from typing import Any

def validate_username(username: str) -> bool:
    """
    Validates the given username.
    
    Args:
    username (str): The username to validate.
    
    Returns:
    bool: True if the username is valid, False otherwise.
    """
    return bool(re.match('^[a-zA-Z0-9_]+$', username))

def validate_email(email: str) -> bool:
    """
    Validates the given email.
    
    Args:
    email (str): The email to validate.
    
    Returns:
    bool: True if the email is valid, False otherwise.
    """
    return bool(re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email))

def validate_password(password: str) -> bool:
    """
    Validates the given password.
    
    Args:
    password (str): The password to validate.
    
    Returns:
    bool: True if the password is valid, False otherwise.
    """
    return bool(re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', password))

def validate_input(data: Any, validation_rules: Dict[str, callable]) -> bool:
    """
    Validates the given input data against the given validation rules.
    
    Args:
    data (Any): The input data to validate.
    validation_rules (Dict[str, callable]): The validation rules to apply.
    
    Returns:
    bool: True if the input data is valid, False otherwise.
    """
    for key, value in data.items():
        if key in validation_rules and not validation_rules[key](value):
            return False
    return True