"""
# Bad practice because we don't know what went wrong
try:
        x = int(input("What's x?"))
        print (f"x is {x}") 
        # we shouldn't put many things in try, only the thing prone to error
        # when error for entering "x", the error happen too soon before the x variable receive value
except ValueError:
        print("x is not an integer")
"""

def main():
        print ("x is", get_int("Yooo "))

def get_int(prompt):
        while True:
                try:
                        return int(input(prompt + "GIMME X? "))
                except ValueError:
                        pass

main()