import json

with open ("balance.json", mode ="r+") as file:
        file.write('{"balance": 100}')
        data = json.load(file)

print("Balance:", data["balance"])
'''
def main():


#Loads existing budget data.
def load_data(): 

#Saves budget data.
def save_data(): 

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