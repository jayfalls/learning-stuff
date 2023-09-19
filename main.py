import random


# VARIABLES
## Bet Parameters
MAX_LINES = int(3)
MAX_BET = int(100)
MIN_BET = int(1)

## Spin Parameters
ROWS = 3
COLLUMS = 3
### Spin Odds
symbol_counts = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


def get_slot_machine_spin(num_rows, num_collumns, symbol_counts):
    all_symbols = []
    # Get a list of every possible symbol
    for symbol, symbol_count in symbol_counts.items(): # Seperate the key, value pairs into their own variables
        # _ for no variable
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    # Randomly pull from all_symbols to populate the collums
    collumns = []
    for _ in range(num_collumns):
        collumn = []
        current_symbols = all_symbols[:] # Make a copy of all_symbols list [:]
        for _ in range(num_rows):
            value = random.choice(current_symbols) 
            current_symbols.remove(value)
            collumn.append(value)
        
        collumns.append(collumn)
    
    return collumns


# Changes the orientation of collumns and rows around
def print_slot_machine(collumns):
    for row_number in range(len(collumns[0])):
        for index, collumn in enumerate(collumns): # Enumerate allows both index and items in a list from a for loop
            if index == len(collumns) - 1:
                print(collumn[row_number], end="")
                continue
            print(collumn[row_number], end=" | ")
        print() # Can also use "\n" to print on next line




# INPUT
## Error Handling
def is_valid_number(string_input):
    if string_input.isdigit():
        return True
    
    print("Please enter a valid number")
    return False
    
## User Values
def get_deposit():
    while True:
        deposit_amount = input("What would you like to deposit? $")
        
        if not is_valid_number(deposit_amount):
            continue

        deposit_amount = int(deposit_amount)
        # Make sure amount is valid
        if deposit_amount == 0:
            print("Amount must be greater than 0")
            continue
        
        break
        
    return deposit_amount

def get_number_of_lines():
    while True:
        num_lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")

        if not is_valid_number(num_lines):
            continue

        num_lines = int(num_lines)
        # Make sure amount of lines are valid
        if not 1 <= num_lines <= MAX_LINES:
            print("lines must be between 1 and " + str(MAX_LINES))
            continue
        
        break
        
    return num_lines

def get_bet():
    while True:
        bet_amount = input("What would you like to bet on each line? $")
        
        if not is_valid_number(bet_amount):
            continue

        bet_amount = int(bet_amount)
        # Make sure amount is valid
        if not MIN_BET <= bet_amount <= MAX_BET :
            print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
            continue
        
        break
        
    return bet_amount


# PROGRAM START
def main():
    bet = 0
    balance = get_deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Your bet of ${total_bet} is more than your balance of ${balance}")
            continue

        break

    print(f"You are betting ${bet} on {lines}. Total bet is: ${total_bet}")

    slots = get_slot_machine_spin(ROWS,COLLUMS,symbol_counts)
    print_slot_machine(slots)

main()