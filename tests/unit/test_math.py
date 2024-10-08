import pytest
 
def test_sum_3_plus_2():
    """
    GIVEN two numbers
    WHEN I sum both numbers
    THEN the calculation should be right
    """
    number_A = 3
    number_B = 2
    result = number_A + number_B
 
    assert result == 5