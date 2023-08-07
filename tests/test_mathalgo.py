from src import mathalgo
 
def test_area():
    output = mathalgo.area_of_rectangle(2,5)
    assert output == 10
 
def test_perimeter():
    output = mathalgo.perimeter_of_rectangle(2,5)
    assert output == 14