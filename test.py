from dataklasses import dataklass

# Example use


@dataklass
class Coordinates:
    x: int
    y: int


a = Coordinates('3', 2)
b = Coordinates(2, 3)
print(a, b)
