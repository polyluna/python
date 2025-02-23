def main():
        x = get_num()
        meow(x)

def get_num():
        while True:
                n = int(input("time to meow"))
                if (n > 0):
                        return n

def meow(m):
        print ("meow " * m)
        #or for _ in range (n):
main()