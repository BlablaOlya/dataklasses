from dataklasses import dataklass


@dataklass
class Coordinates:
    x: float
    y: float


# Correct:
p1 = Coordinates(1, 2)
p2 = Coordinates(x=1.5, y=5.0)

# Wrong:
p3 = Coordinates('a', 'b')
# example.py:15: error: Argument 1 to "Coordinates" has incompatible type "str"; expected "float"
# example.py:15: error: Argument 2 to "Coordinates" has incompatible type "str"; expected "float"

p4 = Coordinates(a=1, b=2)
# example.py:19: error: Unexpected keyword argument "a" for "Coordinates"
# example.py:19: error: Unexpected keyword argument "b" for "Coordinates"
