import hanoy
file=open("test3.txt")
     
def test_check_disk_content():
    result=hanoy.check_disk_content(file)
    assert result == [[[1, 2, 3], [], []],hanoy.number_of_disk,[1, 2, 3]]
    
def test_moves_content():
        result=hanoy.moves
        assert result == [13, 12, 32, 13, 21, 23, 13]
        
def test_check_disk_moves():
        result=hanoy.result_hanoi
        assert result == "YES"