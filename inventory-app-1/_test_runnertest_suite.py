import unittest
from main import *

# Add imports here!
from models import sql_database
from app import app


class UnitTests(unittest.TestCase):

  def test_view_all_items(self):
      # Enter code here
      with app.test_client() as client:
        resp=client.get("/")
        self.assertEqual(resp.status_code,200)

