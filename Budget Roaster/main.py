import json

#def main():
today_budget = int(input("What's your budget today?"))

# Write data def save_data(): 
with open("balance.json", mode="w") as file:
    json.dump({"balance": today_budget}, file)

# Read data def load_data(): 
with open("balance.json", mode="r") as file:
    data = json.load(file)

print(data)

print("Balance:", data["balance"])

c_budget = data["balance"]

while True:
        num = input("Enter a number, or 'done':")
        if num =="done":
             break
        try:
                num = int(num)
                c_budget -= num
                print("remaining budget = ",c_budget)
        except ValueError:
              print("Please input your spending today or 'done'.")

'''

#Gets and validates user input for income.
def get_income(): 

#Handles adding expenses, prevents negative values.
def add_expense(): 


#Computes totals and money left.
def calculate_summary():

#Computes totals and money left.
def display_summary(): 

#Displays random funny messages when overspending.
def show_funny_warning():

if __name__ == "__main__":
        main()'
'''