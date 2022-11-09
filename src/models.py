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
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorite_characters = relationship("Favorite_Characters", back_populates = "user_fav_characters")
    favorite_planets = relationship("Favorite_Planets", back_populates = "user_fav_planets")

    def serialize(self):
        return{
            "id" : self.id,
            "username" : self.username,
            "email" : self.email,
            "password" : self.password
        }    

class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    diameter = Column(String(250), nullable=False)
    name = Column(String(250), nullable=True)
    url = Column(String(250), nullable=True)
    population = Column(String(250) , nullable=False)

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
    name = Column(String(250), nullable=True)
    url = Column(String(250), nullable=True)
    birth_year = Column(String(250), nullable=False)
    homeworld = Column(String(250) , nullable=False)

    def serialize(self):
        return{
            "id" : id.self,
            "name" : name.self,
            "url" : url.self,
            "birth_year" : birth_year.self,
            "homeworld" : homeworld.self
        } 

class Favorite_Planets(Base):
    __tablename__ = 'favorite_planets'   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'), primary_key=True)
    user_fav_planets = relationship("User", back_populates = "favorite_planets")

    def serialize(self):
        return{
            "id" : id.self,
            "user_id" : user_id.self,
            "planet_id" : planet_id.self,            
        }

class Favorite_Characters(Base):
    __tablename__ = 'favorite_character'   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'), primary_key=True)
    user_fav_characters = relationship("User", back_populates = "favorite_characters")

    def serialize(self):
        return{
            "id" : id.self,
            "user_id" : user_id.self,
            "character_id" : character_id.self,            
        }          

    # def to_dict(self):
    #     return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')