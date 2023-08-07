#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """This is representing the BaseModel of the hbnb project"""

    # The __init__() method initializes a new BaseModel instance
    def __init__(self, *args, **kvargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
