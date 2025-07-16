from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    species = Column(String(100), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return f"<Pet(name='{self.name}', species='{self.species}', age={self.age})>"

#движок и сессии
engine = create_engine('sqlite:///shelter.db')
Session = sessionmaker(bind=engine)
db_session = Session()

# Создание таблиц
def init_db():
    Base.metadata.create_all(bind=engine)