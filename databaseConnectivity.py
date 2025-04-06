
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:rohit@localhost:3306/world"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
# Define a model class for the 'city' table
class City(Base):
    __tablename__ = 'city'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(35), nullable=False)
    CountryCode = Column(String(3), nullable=False)
    District = Column(String(20), nullable=False)
    Population = Column(Integer)

# Create tables in the database (if they don't exist already)
Base.metadata.create_all(engine)

# Create a session to interact with the DB
Session = sessionmaker(bind=engine)
session = Session()

# Example: Query all cities
cities = session.query(City).all()
for city in cities:
    print(city.ID, city.Name, city.CountryCode, city.District, city.Population)



