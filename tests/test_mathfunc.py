from src import mathfunc
 
def test_calc_addition():
    # Verify the output of `calc_addition` function
    output = mathfunc.calc_addition(2,4)
    assert output == 6
 
def test_calc_substraction():
    # Verify the output of `calc_substraction` function
    output = mathfunc.calc_substraction(2, 4)
    assert output == -2
     
def test_calc_multiply():
    # Verify the output of `calc_multiply` function
    output = mathfunc.calc_multiply(2,4)
    assert output == 8