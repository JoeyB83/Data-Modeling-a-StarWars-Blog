import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)

    def serialize(self):
        return{
            "id" : self.id,
            "username" : self.username,
            "email" : self.email
        }

    #     "properties": {
    #   "diameter": "10465",
    #   "rotation_period": "23",
    #   "orbital_period": "304",
    #   "gravity": "1 standard",
    #   "population": "200000",
    #   "climate": "arid",
    #   "terrain": "desert",
    #   "surface_water": "1",
    #   "created": "2022-10-24T08:31:56.449Z",
    #   "edited": "2022-10-24T08:31:56.449Z",
    #   "name": "Tatooine",
    #   "url": "https://www.swapi.tech/api/planets/1"
    # },
    # "description": "A planet.",

class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True, unique=True)
    url = Column(String(150), nullable=True)
    diameter = Column(String(15), nullable=False)
    population = Column(String(18) , nullable=False)

    def serialize(self):
        return{
            "id" : id.self,
            "name" : name.self,
            "url" : url.self,
            "diameter" : diameter.self,
            "population" : population.self
        }

class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True, unique=True)
    url = Column(String(150), nullable=True)
    birth_year = Column(String(15), nullable=False)
    homeworld = Column(String(18) , nullable=False)

    def serialize(self):
        return{
            "id" : id.self,
            "name" : name.self,
            "url" : url.self,
            "birth_year" : birth_year.self,
            "homeworld" : homeworld.self
        }        



# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')