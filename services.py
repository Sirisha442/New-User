from utils import validate_password, hash_password
from database import Session
from models import User
from datetime import datetime

def add_user(first_name, last_name, email, date_of_birth, password):
    session = Session()
    try:
        # Check if user already exists
        existing_user = session.query(User).filter(User.email == email).first()
        if existing_user:
            return "Customer already exists"

        # Get age from date of birth
        birth_date = datetime.strptime(date_of_birth, "%Y-%m-%d")
        age = (datetime.now() - birth_date).days // 365

        # Validate password
        used_passwords = [u.password for u in session.query(User).all()]
        validation_error = validate_password(password, used_passwords)
        if validation_error:
            return validation_error

        # Add new user
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            date_of_birth=birth_date,
            age=age,
            password=hash_password(password)
        )
        session.add(new_user)
        session.commit()
        return "User successfully created"
    except Exception as e:
        session.rollback()
        return f"An error occurred: {e}"
    finally:
        session.close()

