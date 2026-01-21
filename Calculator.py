#Type casting in Python refers to the process of converting a value from one data type to another. 
# This is often necessary when performing operations that require specific data types or when handling user input, which is typically received as strings. 
a = int (input("Enter the first number:"))
b = int (input("Enter the second number:"))

print ("The sum is: " + str(a + b))

print ("The ans is: " + str(a - b))


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length
    
square = Square(4)
print(square.area())

rectangle = Rectangle(2,4)
print(rectangle.area())

