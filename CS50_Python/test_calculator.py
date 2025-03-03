from calculator import square

def main():
        test_square()

'''
def test_square():
        if square(2) !=4:
                print ("2 squared is not 4")
        if square(3) !=9:
                print ("3 squared is not 9")
'''
def test_square():
        assert square(2) == 4
        assert square(3) == 9
# can run this with pytest test_calculator.py command

'''
def test_square():
        try:
                assert square(2) ==4
        except: AssertionError:
                print("2 squared is not 4)
'''

if __name__ == "__main__":
        main()
