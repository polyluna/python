import sys

if len(sys.argv) < 2:
        sys.exit("Too few argument")
elif len(sys.argv) >2:
        sys.exit("Too many arguments")

print ("hello, my name is", sys.argv[1])

""" also can
for arg in sys.argv[1:]:
        print("hi", arg)

"""

# you can run this with python name.py ploy