class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def recArea(self):
        return self.a * self.b

rectangle = Rectangle(12, 43)
print(rectangle.recArea())