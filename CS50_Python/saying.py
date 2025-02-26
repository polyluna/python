def main():
        hello("world")
        goodbye("world")

def hello(name):
        print(f"hello,{name}")
def goodbye(name):
        print(f"goodbye,{name}")

if __name__ == "__main__":
        main()
# so function can be imported to other files without running main
# from sayings import hello