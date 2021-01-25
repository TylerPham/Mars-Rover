from Plateau import Plateau
from Rover import Rover
import unittest

ROVER_NAME = 'Sojourner'

class testRover(unittest.TestCase):
    def setUp(self):
        self.plateau = Plateau(5, 5)
        self.rover = Rover(ROVER_NAME)

    def testLanding(self):
        self.rover.land(self.plateau, 3, 4, 'N')
        self.assertEqual(3, self.rover.x)
        self.assertEqual(4, self.rover.y)
        self.assertEqual(ROVER_NAME, self.rover.name)

    def testInvalidLanding(self):
        with self.assertRaises(Exception):
            self.rover.land(self.plateau, 999, 4, 'N')
        with self.assertRaises(Exception):
            self.rover.land(self.plateau, 4, 999, 'N')
        with self.assertRaises(Exception):
            self.rover.land(self.plateau, 4, 4, 'INVALID DIRECTION')

    def testLeftTurn(self):
        self.rover.land(self.plateau, 3, 3, 'N')
        self.rover.turnLeft()
        self.rover.turnLeft()
        self.assertEqual('S', self.rover.direction)


    def testRightTurn(self):
        self.rover.land(self.plateau, 3, 3, 'N')
        self.rover.turnRight()
        self.rover.turnRight()
        self.assertEqual('S', self.rover.direction)

    def testExecuteInstructions(self):
        self.rover.land(self.plateau, 3, 3, 'N')
        self.rover.executeInstructions('LLMRRM')
        self.assertEqual(3, self.rover.x)
        self.assertEqual(3, self.rover.y)

        with self.assertRaises(Exception):
            self.rover.executeInstructions('MMMMMMMM')

    def testGetCoordinateAndBearing(self):
        self.rover.land(self.plateau, 3, 3, 'N')
        self.assertEqual(ROVER_NAME + ':3 3 N', self.rover.getCoordinateAndBearing())

    def testRoverMovingOutOfLimits(self):
        self.rover.land(self.plateau, 5, 5, 'N')
        with self.assertRaises(Exception):
            self.rover.moveForward()

if __name__ == '__main__':
    unittest.main()
