MAX_LINES = int(3)
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        deposit_amount = input("What would you like to deposit? $")
        # Checks if it is a number that is greater than -1
        if not deposit_amount.isdigit():
            print("Please enter a valid number")
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
        # Checks if it is a number that is greater than -1
        if not num_lines.isdigit():
            print("Please enter a valid number")
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
        # Checks if it is a number that is greater than -1
        if not bet_amount.isdigit():
            print("Please enter a valid number")
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
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Your bet of ${total_bet} is more than your balance of ${balance}")
            continue

        break

    print(f"You are betting ${bet} on {lines}. Total bet is: ${total_bet}")

main()