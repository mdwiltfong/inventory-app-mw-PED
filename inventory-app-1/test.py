from unittest import TestCase
from app import app

from flask import request,session
from app import app

from models import db,connect_db

from dotenv import load_dotenv, find_dotenv

class test_crud(TestCase):
    """Get request should return HTML with all items from test db"""
    def test_view(self):
        with app.test_client() as client:
            
