"""
 This is a doc string: 
 Here where info about the purpose of this code goes
"""

def square(x: float) -> float:
    """
    This function computes the square of x
    """
    return x**2

def cube(x: float) -> float:
    """
    This function computes the  cube of x
    """
    return x**3


def main():
    """
    This should be the entry of the application
    """
    x = 12.3
    print(square(x))
    print(cube(x))


if __name__ == '__main__':
    main()


