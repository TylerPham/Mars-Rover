from Plateau import Plateau

class Rover:
    def __init__(self, name: str):
        self.name = name
        self.plateau = None
        self.x = None
        self.y = None
        self.direction = None

    def land(self, plateau: Plateau, xCoordLanding: int, yCoordLanding: int, direction: str):
        if not plateau.isValidCoordinate(xCoordLanding, yCoordLanding):
            raise Exception("Invalid landing coord: [{}, {}] in plateau: [{}, {}]").format(xCoordLanding, yCoordLanding, plateau.xCoordMax, plateau.yCoordMax)
        if not direction in ['N', 'E', 'S', 'W']:
            raise Exception("Invalid direction")

        self.plateau = plateau
        self.x = xCoordLanding
        self.y = yCoordLanding
        self.direction = direction

    def turnLeft(self):
        if self.direction == 'N': self.direction = 'W'
        elif self.direction == 'E': self.direction = 'N'
        elif self.direction == 'S': self.direction = 'E'
        elif self.direction == 'W': self.direction = 'S'

    def turnRight(self):
        if self.direction == 'N': self.direction = 'E'
        elif self.direction == 'E': self.direction = 'S'
        elif self.direction == 'S': self.direction = 'W'
        elif self.direction == 'W': self.direction = 'N'

    def moveForward(self):
        xMove, yMove = 0, 0
        if self.direction == 'N': yMove += 1
        elif self.direction == 'E': xMove += 1
        elif self.direction == 'S': yMove -= 1
        elif self.direction == 'W': xMove -= 1

        if not self.plateau.isValidCoordinate(self.x + xMove, self.y + yMove):
            raise Exception('Invalid movement')

        self.x, self.y = self.x + xMove, self.y + yMove

    def executeInstructions(self, instructionStream: str):
        for instruction in instructionStream:
            if instruction == 'L':
                self.turnLeft()
            elif instruction == 'R':
                self.turnRight()
            elif instruction == 'M':
                self.moveForward()
            else:
                raise Exception('Invalid instruction')

    def getCoordinateAndBearing(self):
        return '{}:{} {} {}'.format(self.name, self.x, self.y, self.direction)
