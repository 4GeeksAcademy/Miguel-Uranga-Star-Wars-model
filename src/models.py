import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, DateTime, Boolean
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    # Datos del Usuario
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True) 
    email = Column(String(120), unique=True, nullable=False)
    username = Column(String(60), unique=True, nullable=False)
    password = Column(String(120), unique=False, nullable=False)
    password_reset = Column(String(4), unique=True, nullable=True)
    password_reset_date = Column(String(120), unique=True, nullable=True)
    is_active = Column(Boolean(), unique=False, nullable=False)

    
    #Foreign keys
    favorite = relationship("Favorites", back_populates = "user", lazy = True)

class Planets(Base):
    # Datos del Hotel
    __tablename__ = 'planets'
    id_planet = Column(Integer, primary_key=True) 
    weather = Column(String(140), nullable= False)
    galaxy = Column(String(140), nullable= False)
    population = Column(String(140), nullable= False)
    diameter =  Column(Integer, nullable = False) 
    rotation_period =  Column(Integer, nullable = False) 
    orbital_period = Column(Integer, nullable = False) 
    gravity = Column(Integer, nullable = False)

    favorite = relationship("Favorites", back_populates = "planet", lazy = True) 

class Characters(Base):
    __tablename__ = 'characters'
    id_character = Column(Integer, primary_key=True) 
    character_planet = Column(Integer, ForeignKey(Planets.id_planet))
    planet = relationship(Planets)
    gender = Column(String(20), nullable= False)
    hair_color = Column(String(20), nullable= False)
    skin_color = Column(String(20), nullable= False)
    eye_color = Column(String(20), nullable= False)
    birth_year = Column(String(20), nullable= False)

    favorite = relationship("Favorites", back_populates = "character", lazy = True)

    

class Favorites(Base):
    __tablename__ = 'favorites'
    id_favorites = Column(Integer, primary_key=True) 
    user_favorites = Column(Integer, ForeignKey(User.id_user))
    user = relationship(User)
    favorite_planet = Column(Integer, ForeignKey(Planets.id_planet))
    planet = relationship(Planets)
    favorite_character = Column(Integer, ForeignKey(Characters.id_character))
    character = relationship(Characters)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e