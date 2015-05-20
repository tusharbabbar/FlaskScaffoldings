import os
import unittest

from app import app

class FirstTest(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
    
    def tearDown(self):
        pass

    def test_api_hello(self):
        rv = self.app.get('/helloapi')
        assert rv.status_code == 200

    def test_blueprint_hello(self):
        rv = self.app.get('/my_blueprint/helloblu')
    
if __name__ == '__main__':
    unittest.main()

