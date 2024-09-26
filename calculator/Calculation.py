class Calculation:
    def __init__(self, x, y, operation):
        self.x = x
        self.y = y
        self.operation = operation

    def Output(self):
        return self.operation(self.x, self.y)
