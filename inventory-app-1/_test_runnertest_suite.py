import unittest
from main import *

# Add imports here!
from models import sql_database
from app import app
''' These functions are related to Replit's built in unit test feature. 
At the time of running this the unit test feature was consistently failing,
yet tests were able to be developed and ran locally. 
  '''

class UnitTests(unittest.TestCase):

  def test_view_all_items(self):
      # Enter code here
      with app.test_client() as client:
        resp=client.get("/")
        self.assertEqual(resp.status_code,200)

