import re
import hashlib

# Validate password
def validate_password(password, used_passwords):
    if len(password) < 8:
        return "Password must be at least 8 characters long"
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter"
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter"
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit"
    if not any(char in "!@#$%^&*()-_=+" for char in password):
        return "Password must contain at least one special character"
    hashed_password = hash_password(password)
    if hashed_password in used_passwords:
        return "Password has already been used"
    return None

# Hash password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
