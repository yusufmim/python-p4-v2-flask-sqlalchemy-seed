#!/usr/bin/env python3
#server/seed.py

from app import app
from models import db, Pet
from faker import Faker
from random import choice as rc

with app.app_context():
    Pet.query.delete()  # clear table first
    pets = [
        Pet(name="Fido", species="Dog"),
        Pet(name="Whiskers", species="Cat"),
        Pet(name="Hermie", species="Hamster"),
        Pet(name="Slither", species="Snake")
    ]
    db.session.add_all(pets)

    db.session.commit()

fake = Faker()
species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

for _ in range(10):
    name = fake.first_name()
    type = rc(species)
    pets.append(Pet(name=name, species=type))