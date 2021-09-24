def DIV(a, b):
    return a/b
 
def test_floatTest():
   assert type(DIV(8, 2)) is float

def test_floatTest1():
   assert "." in str(DIV(5, 5))

def test_floatTest2():
   def floatTest():
    try:
        assert (5)
    except Exception:
        pass

