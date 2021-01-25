class Plateau:
    def __init__(self, xCoordMax: int, yCoordMax: int):
        self.xCoordMax = xCoordMax
        self.yCoordMax = yCoordMax

    def isValidCoordinate(self, x: int, y: int):
        return True if x >= 0 and x <= self.xCoordMax and y >=0 and y <=self.yCoordMax else False

