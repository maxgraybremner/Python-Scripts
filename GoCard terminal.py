## GoCard terminal.py ##
## The goal of this task was to create a simple gocard terminal which takes 4 simple commands
## initially the user is asked for the initial balance of the go card
## then they have the option to input 4 commands 
## r - this counts as a ride and reduces the balance by a certain amount
## t - this counts as a top-up and increases the balance by a certain amount
## b - displays the balance 
## q - displays all the events that have occured along with the cost/top-up amount and the balance after the event 

## create a class for a transportation class which takes only on argumnet, the initial balance
class gocard:

    def __init__(self, x):
        self.balance = x
    
    def __str__(self): ## this returns the current balance when the "b" command is input
        return f"Balance = ${self.balance}"

    def add_balance(self, topup: float): ## this add the top up value to the balance when the "t" command is input
        self.balance = self.balance + topup
        return ["Top up", topup, usr_card.balance] ## returns a list of values for the final statement 

    def red_balance(self, reduction: float): ## this reduces the balance when the "r" command is input
        self.balance = self.balance - reduction
        return ["Ride", float(reduction), usr_card.balance] ## returns a list of values for the final statement 
    

## print the final statement
def printStatement(balance: float, events: list):
    statement.append(["Final balance", '', balance]) ## append the final balance values
    print("Statement:") ## header
    cols = ['event', 'amount ($)', 'balance ($)'] 
    col_format = "{:<20} {:>20} {:>20}" ## format of the columns
    print(col_format.format(*cols)) ## print header columns

    for ev, am, bal in events: ## print the values from the event list 
        print(col_format.format(ev, am, bal))
     

## create the gpcard instance and set the balance to a float value 
usr_card = gocard(float(input("Creating account. Input initial balance: ")))
usr_input = "" ## initiate the command input
statement = ["Initial balance", '', usr_card.balance] ## initiate the events list with the initial balance

##
while usr_input != "q":
    print("?", end= " ")
    usr_input = input().lower() ## take the user command and convert to lowercase
    usr_cmd = usr_input.split()[0] ## take the user command

    if usr_cmd == 'r': ## reduce the balance
        cost = usr_input.split(" ")[1]

        if cost.replace('.', '').isdigit(): ## check that the value is a number (the replace function is used to include float values)
            statement.append(usr_card.red_balance(float(cost))) ## add the event to the events list 
        else:
            print("Bad command.")
        
    elif usr_cmd == 'b':
        print(usr_card)

    elif usr_cmd == 't':
        payment = usr_input.split()[1]

        if payment.replace('.', '').isdigit(): ## check that the value is a number (the replace function is used to include float values)
            statement.append(usr_card.add_balance(float(payment))) ## add the event to the events list 
        else:
            print("Bad command.")

    elif usr_cmd == 'q':
        printStatement(usr_card.balance, statement) ## print the final statement
    else:
        print("Bad Command.")




