from fastapi import FastAPI, HTTPException
from services import add_user
from database import initialize_database

# Initialize the database
initialize_database()

# Create the FastAPI app
app = FastAPI()

# Define the API endpoint for user registration
@app.post("/register")
async def register_user(
    first_name: str,
    last_name: str,
    email: str,
    date_of_birth: str,
    password: str
):
    response = add_user(first_name, last_name, email, date_of_birth, password)
    if response != "User successfully created":
        raise HTTPException(status_code=400, detail=response)
    return {"message": response}

