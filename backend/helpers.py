import json
from typing import Any

def format_error_response(code: int, message: str) -> str:
    """
    Formats an error response.
    
    Args:
    code (int): The error code.
    message (str): The error message.
    
    Returns:
    str: The formatted error response.
    """
    return json.dumps({'error': {'code': code, 'message': message}})

def format_success_response(data: Any) -> str:
    """
    Formats a success response.
    
    Args:
    data (Any): The data to return.
    
    Returns:
    str: The formatted success response.
    """
    return json.dumps(data)
# Create a JWT token
token = create_jwt_token(1, 'john_doe', 'john@example.com', 'secret_key')

# Verify a JWT token
payload = verify_jwt_token(token, 'secret_key')
if payload:
    print('Token is valid')
else:
    print('Token is invalid')

# Validate a username
if validate_username('john_doe'):
    print('Username is valid')
else:
    print('Username is invalid')

# Validate an email
if validate_email('john@example.com'):
    print('Email is valid')
else:
    print('Email is invalid')

# Validate a password
if validate_password('P@ssw0rd'):
    print('Password is valid')
else:
    print('Password is invalid')

# Validate input data
data = {'username': 'john_doe', 'email': 'john@example.com'}
validation_rules = {'username': validate_username, 'email': validate_email}
if validate_input(data, validation_rules):
    print('Input data is valid')
else:
    print('Input data is invalid')

# Format an error response
error_response = format_error_response(400, 'Invalid request')
print(error_response)

# Format a success response
success_response = format_success_response({'message': 'Request successful'})
print(success_response)