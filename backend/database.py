from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://postgres:project%401@localhost:5432/featureflag_db"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

if __name__ == "__main__":
    try:
        engine.connect()
        print("Database connected successfully")
    except Exception as e:
        print("Database connection failed:", e)
