import unittest
from ping import *
result = ping ("google.com")


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.result = ping ("google.com")

    def test_packet_loss(self):
        self.assertTrue("packet loss" in self.result)

    def test_number_ping(self):
        self.assertRaises(TypeError, ping, 12312312)

    def test_list_ping(self):
        self.assertRaises(TypeError, ping, [1,2,3,4,5])

    def test_tuple_ping(self):
        self.assertRaises(TypeError, ping, (1,2,3,4,5))

if __name__ == '__main__':
    unittest.main()
