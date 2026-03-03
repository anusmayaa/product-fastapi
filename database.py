import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 1. Load the secrets from your .env file
load_dotenv()

# 2. Use your variable name 'db_url' but get the value from the environment
db_url = os.getenv("DATABASE_URL")

# 3. Your original logic
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Added this so your Product model has a Base to inherit from
Base = declarative_base()