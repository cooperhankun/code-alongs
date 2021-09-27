import matplotlib.pyplot as plt

class Vector:
    """ A class to represent a Euclidean vector with magnitude and direction"""

    # in Python >= 3.10 - can use float | int in annotation
    def __init__(self, *numbers: float) -> None:  # *numbers is variadic parameter
        # error checking
        for number in numbers:
            if not isinstance(number, (float, int)):
                raise TypeError(f"{number} is not valid number in a vector")

        if len(numbers) <= 0:
            raise ValueError("Vector can't be empty")

        # to take care of booleans
        self._numbers = tuple(float(number) for number in numbers)

    @property
    def numbers(self) -> tuple:
        return self._numbers

    def __add__(self, other: "Vector") -> "Vector":
        if self.validate_vectors(other):
            numbers = (a+b for a, b in zip(self.numbers, other.numbers))
            return Vector(*numbers)

    def __sub__(self, other: "Vector") -> "Vector":
        if self.validate_vectors(other):
            numbers = (a-b for a, b in zip(self.numbers, other.numbers))
            return Vector(*numbers)

    def __mul__(self, value: float) -> "Vector":
        print("__mul__ is called")
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"The value for multiplication must be int or float not {type(value)}")
        numbers = (value*a for a in self.numbers)
        return Vector(*numbers)

    # to make multiplication commutative, i.e. a*v = v*a
    def __rmul__(self, value: float) -> "Vector":
        print("__rmul__ is called ...")
        return self*value

    # for using len() method on a Vector object
    def __len__(self) -> int:
        """ Returns number of components in a Vector not the length"""
        return len(self.numbers)

    def norm(self) -> float:
        """ Returns the Euclidean norm of a Vector"""
        return sum(a**2 for a in self.numbers)**.5

    def validate_vectors(self, other: "Vector") -> bool:
        """ validates if two vectors have same length """
        if not isinstance(other, Vector) or len(other) != len(self):
            raise TypeError(f"Both must be Vector and have the same length")
        return len(self) == len(other)

    def __getitem__(self, item: int) -> float:
        return self.numbers[item]

    def plot(self, *others: "Vector") -> None:
        """ Visualize vectors """
        X, Y = [], []

        for vector in tuple(others):
            if Vector.is2D(vector) and Vector.is2D(self):
                X.append(vector[0])
                Y.append(vector[1])
        
        X.append(self[0])
        Y.append(self[1])

        originX = originY = tuple(0 for _ in range(len(X)))

        plt.quiver(originX, originY, X, Y, scale=1,
                   scale_units="xy", angles="xy")
        plt.xlim(-2, 10)
        plt.ylim(-2, 10)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"{self}, {others}")
        plt.grid()
        plt.show()

        # TODO: make xlim and ylim adapt after the vectors dimensions 
        # TODO: fix title paranthesis

    @staticmethod # bound to the class and not dependent on the object itself
    def is2D(vector: "Vector") -> bool:
        if len(vector) != 2:
            raise ValueError(
                f"Vector dimension must be 2 not {len(vector)}")
        return True

    def __repr__(self) -> str:
        return f"Vector{self.numbers}"

    # NOTE: There are many more features to be implemented, feel free to do it
    # TODO: implement norm between vectors
    # TODO: implement dot product
    # TODO: implement vector product
    # TODO: implement conjugate 
    # TODO: implement projection

v1 = Vector(2, 3, 51.5, 67, True)
print(v1)
print(f"len(v1): {len(v1)}")

v2 = Vector(1, 2)
try:
    v1+v2
except TypeError as err:
    print(err)

v3 = Vector(2, 2)

v_23 = v3+v2
print(v_23)
v_23.norm()

print(v3*2)
# 2*v3 not work if you haven't implemented __rmul__()
2*v3

a = Vector(3,4)
b = Vector(2,5)
c = a + b 

c.plot(a,b)
