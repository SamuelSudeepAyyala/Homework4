class Calculation:
    result = None
    def __init__(self, operation, x, y):
        self.operation = operation
        self.x = x
        self.y = y

    def get_result(self):
        result = self.operation(self.x, self.y)
        return result
    
    def __str__(self):
        return f"{self.operation} {self.x} and {self.y} = {self.result}"
