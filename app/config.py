import os
from dotenv import load_dotenv

try:
    load_dotenv()
except Exception as e:
    print(f"Error loading .env file: {e}")

# Access the variables
SECRET_KEY = os.getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

# Now you can use SECRET_KEY and SQLALCHEMY_DATABASE_URI in your application
