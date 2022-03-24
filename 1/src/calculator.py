class Calculator:
    def add(self, x, y):
        checkVariables(x, y)
        return x + y

    def subtract(self, x, y):
        checkVariables(x, y)
        return x - y

    def multiply(self, x, y):
        checkVariables(x, y)
        return x * y

    def divide(self, x, y):
        checkVariables(x, y)
        return x / y

def checkVariables(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Wrong input!")