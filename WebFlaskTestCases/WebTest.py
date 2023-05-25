import unittest
from WebApp import app

class testWebClass(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    
    def test_welcome(self):
        respValue= self.app.get("/")
        # self.assertEqual(Data,Output)
        print(respValue.data)
        # self.assertEqual(respValue.data,"Welcome to Python Project")

if __name__ ==  '__main__':
    unittest.main()