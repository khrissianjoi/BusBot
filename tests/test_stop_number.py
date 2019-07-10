import sys
import os

absFilePath = os.path.abspath(__file__)
fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)
sys.path.append(parentDir)

import unittest

from bus_bot import get_request

class StopNumberTest(unittest.TestCase):
    def test1(self):
        stop_id = '4793'
        current = {
            'stopid' : stop_id, 
            'format' :'json'
        }
        self.assertEqual(get_request(current)[1], 200)

    def test2(self):
        stop_id = 'ABDS'
        current = {
            'stopid' : stop_id, 
            'format' :'json'
        }
        self.assertNotEqual(get_request(current)[1], 200)
    
    def test3(self):
        stop_id = '9999999'
        current = {
            'stopid' : stop_id, 
            'format' :'json'
        }
        self.assertEqual(get_request(current), 'Sorry human, please enter a real bus stop number')

if __name__ == "__main__":
    unittest.main()