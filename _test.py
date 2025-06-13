import pytest 

#Function to test the square

def square(n):
    return n**2

def cube(n):
    return n**3

def fifth_power(n):
    return n**5



# Testing the Square Function
def test_square():
    assert square(2) == 4, "Test failed should have been 4"
    assert square(3) == 9, "Test failed should have been 9"

# Testing the Cube Function
def test_cube():
    assert cube(2) == 8, "Test failed should have been 8"
    assert cube(3) == 27, "Test failed should have been 27"

# Testing the Fifth Power Function
def test_power5():
    assert fifth_power(2) == 32, "Test failed should have been 32"
    assert fifth_power(3) == 243, "Test failed should have been 243"


def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")