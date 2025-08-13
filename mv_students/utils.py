import hashlib
from django.utils.crypto import get_random_string

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()    


