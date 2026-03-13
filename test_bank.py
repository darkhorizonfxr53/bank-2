from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_h_start():
    assert value("hi") == 20
    assert value("Hey there") == 20

def test_other():
    assert value("Greetings") == 100
    assert value("What's up") == 100
