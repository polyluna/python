from hello import hello

def test_hello():
        assert hello("David") == "hello, David"

def test_argument():
        for name in ["Hermione", "Harry", "Ron"]
        assert hello(name) ==f"hello,{name}"