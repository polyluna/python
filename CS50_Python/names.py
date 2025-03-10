name = input("Gimme name")


#file = open("names.txt", "a")
#file.write(f"{name}\n")
#file.close()

with open("name.txt", "a") as file:
        file.write(f"{name}\n")