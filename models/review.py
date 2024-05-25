#!/usr/bin/python3
'''a model class review'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''class Review that inherits from BaseModel'''
    place_id = ""
    user_id = ""
    text = ""
