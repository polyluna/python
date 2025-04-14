import json

def main():
        today_budget = int(input("What's your budget today?"))
        save_data(today_budget)
        data = load_data()
        c_budget = data["balance"]

        while True:
                num = input("So tell me now, how much did you spent?, or 'done':")
                if num =="done":
                        break
                try:
                        num = int(num)
                        c_budget -= num
                        if c_budget <= 0:
                                print("OVER BUDGET! --> YOU ARE EATING INSTANT NOODLES TMR")
                                break
                        print(rxn(num))
                        print("remaining budget = ",c_budget)
                        
                except ValueError:
                        print("Please input your spending today or 'done'.")

# Write data 
def save_data(td_budget): 
        with open("balance.json", mode="w") as file:
                json.dump({"balance": td_budget}, file)


# Read data 
def load_data(): 
        with open("balance.json", mode="r") as file:
                return json.load(file)

        #print(data)
        #print("Balance:", data["balance"])


def rxn(num):
        if 0 <= num <= 20:
              return "okayy..." 
        if 20 <= num <= 75:
              return "coffee or a meal or smt mhmm..." 
        if 75 <= num <= 300:
              return "you're quite a spendthrift today huh?" 
        else:   
              return "Shopping day?"
      
if __name__ == "__main__":
      main()      
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