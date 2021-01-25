import unittest
from Plateau import Plateau

class testPlateau(unittest.TestCase):
    def setUp(self):
        self.plateau = Plateau(5, 5)

    def test_valid_position(self):
        self.assertTrue(self.plateau.isValidCoordinate(0,0))
        self.assertTrue(self.plateau.isValidCoordinate(5,5))
        self.assertFalse(self.plateau.isValidCoordinate(6,0))
        self.assertFalse(self.plateau.isValidCoordinate(0,6))
        self.assertFalse(self.plateau.isValidCoordinate(-1,-1))

if __name__ == '__main__':
    unittest.main()
