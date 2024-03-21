from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Replace 'sqlite:///restaurant_reviews.db' with your actual database URL
DATABASE_URL = 'sqlite:///restaurant_reviews.db'

# Create a database engine
engine = create_engine(DATABASE_URL)

# Create the tables if they don't exist
Base.metadata.create_all(engine)

# Create a sessionmaker
Session = sessionmaker(bind=engine)

# Function to create a new session
def create_session():
    return Session()

if __name__ == "__main__":
    # Code to run when executing this file directly
    print("Database setup complete.")
