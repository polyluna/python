name = input ("What's your name? ")

match name:
        case "Harry" | "Hermione":
                print("Griffindor")
        case "Draco":
                print("Slytherin")
        case _:
                print("who?")