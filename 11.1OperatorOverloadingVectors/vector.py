class Vector:
    """ A class to represent a eulicdean vector with magnitude and direction"""

    def __init__(self, *numbers) -> None:
        # print(numbers)
        for number in numbers:
            if not isinstance(number, (float, int)):
                raise TypeError(f"{number} must be float or int not {type(number)}")
            
        if len(numbers)  <= 0:
            raise ValueError("Vector can not ne empty")

        self._numbers = tuple(float(number) for number in numbers)


    @property
    def numbers(self) -> tuple:
        return self._numbers

    # (2,3) + (1,1,1) not ok
    # (2,3) + (1,1) = (3,3) ok
    def __add__(self, other: "Vector") -> "Vector":
        if self.validate_vectors(other):
            numbers = (a+b for a,b in zip(self.numbers, other.numbers))
            return Vector(*numbers)

    def __len__ (self) -> int:
        return len(self.numbers)
    
    def validate_vectors(self, other: "Vector") -> bool:
        """ validate that two vectors have same dimensions """
        if not isinstance(other, Vector) or len(other) != len(self):
            raise TypeError("both must be Vector and same length")
        return len(self) == len(other)

    def __repr__(self) -> str:
        return f"Vector{self.numbers}"

    def __str__(self) -> str:
        return f"{self.numbers}"
        
# [] operator
    def __getitem__(self, item: int) -> float:
        return self.numbers[item]




