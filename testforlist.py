list = [1,2,3,4,5]
 
def lgt(): 
    return len(list)
   
def test_listTest():
    assert len(list) is lgt()

def test_listTest1():
    list.append(3)
    assert len(list) is lgt()

def test_listTest2():
    assert 3 in list


