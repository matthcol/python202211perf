from point import WeightedColoredPoint

def test_constructor_allArgs():
    wcp = WeightedColoredPoint("WCP", 10, 11, 4.5, 'green')
    assert wcp.name == "WCP"
    assert wcp.x == 10
    assert wcp.y == 11
    assert wcp.weight == 4.5
    assert wcp.color == 'green'