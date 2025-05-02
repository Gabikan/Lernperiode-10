from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Sneaker(Base):
    __tablename__ = 'sneakers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
    color = Column(String, nullable=False)
    type = Column(String, nullable=False)
    brand_id = Column(Integer, ForeignKey('brands.id'))

    brand = relationship("Brand")

engine = create_engine('sqlite:///sneakerstore.db')
Base.metadata.create_all(engine)
