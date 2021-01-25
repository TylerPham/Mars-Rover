from Plateau import Plateau
from Rover import Rover
import sys

def parsePlateau(input):
    x, y = input.strip('Plateau:').split()
    return int(x), int(y)

def parseLanding(input):
    roverName, x, y, direction = input.replace('Landing:', '').split(' ')
    return roverName, int(x), int(y), direction

def parseInstructions(input):
    roverName, instructions = input.replace('Instructions:', '').split(' ')
    return roverName, instructions

if __name__ == '__main__':
    for line in sys.stdin:
        command = line.rstrip()
        if len(command) == 0:
            continue
        if 'Plateau:' in command:
            x, y = parsePlateau(command)
            plateau = Plateau(x, y)
        elif 'Landing:' in command:
            roverName, x, y, direction = parseLanding(command)
            rover = Rover(roverName)
            rover.land(plateau, x, y, direction)
        elif 'Instructions:' in command:
            _, instructions = parseInstructions(command)
            rover.executeInstructions(instructions)
            print(rover.getCoordinateAndBearing())
        else:
            print('invalid line')

