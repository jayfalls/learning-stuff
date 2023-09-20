import asyncio
import random
import sys


# VARIABLES
## Bet Parameters
MAX_LINES: int = 3
MAX_BET: int = 100
MIN_BET: int = 1

## Spin Parameters
ROWS: int = 3
COLLUMNS: int = 3
### Spin Odds
symbol_counts: dict[str, int] = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_values: dict[str, int] = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


# SPINS
def get_all_symbols(symbol_counts: dict[str, int]) -> list[str]:
    all_symbols: list[str] = []
    # Get a list of every possible symbol
    for symbol, symbol_count in symbol_counts.items(): # Seperate the key, value pairs into their own variables
        # _ for no variable
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    return all_symbols

def draw_random_symbols(num_rows: int, num_collumns: int, all_symbols: list[str]) -> list[list[str]]:
    # Randomly pull from all_symbols to populate the collums
    collumns: list[list[str]] = []
    for _ in range(num_collumns):
        collumn: list[str] = []
        current_symbols: list[str] = all_symbols[:] # Make a copy of all_symbols list [:]
        for _ in range(num_rows):
            symbol: str = random.choice(current_symbols) 
            current_symbols.remove(symbol)
            collumn.append(symbol)
        
        collumns.append(collumn)
    
    return collumns

## Changes the orientation of collumns and rows around
def reorder_collums(drawn_collumns: list[list[str]]) -> list[list[str]]:
    final_lines: list[list[str]] = []
    for row_number in range(len(drawn_collumns[0])):
        single_line: list[str] = []
        for collumn in drawn_collumns: 
            single_line.append(collumn[row_number])
        final_lines.append(single_line)
    return final_lines

async def check_winnings(final_lines: [list[list[str]]], num_lines: int, bet: int) -> int:
    winnings: int = 0
    # Counts starting from the first line
    for line in range(num_lines):
        symbol: str = final_lines[line][0]
        single_line: list[str] = final_lines[line]
        for symbol_index in range(len(single_line)):
            symbol_to_check = single_line[symbol_index]
            if symbol != symbol_to_check:
                break
        else:
            winnings += symbol_values[symbol] * bet
    
    return winnings

## Draws and prints out the slots
async def printout_slots(final_lines: list[list[str]]) -> None: 
    for line in final_lines:
        for index, symbol in enumerate(line): # Enumerate outputs variables for both index and items in a list
            if index == len(line) - 1:
                print(symbol, end="")
                continue
            print(symbol, end=" | ")
            sys.stdout.flush()  # Force immediate display
            await asyncio.sleep(random.uniform(0.5, 1.5))
        print() # Can also use "\n" to print out to next line
        await asyncio.sleep(1)  

async def spin_user_animation(final_lines: [list[list[str]]], num_lines: int, bet: int) -> int:
    checking_winnings = asyncio.create_task(check_winnings(final_lines, num_lines, bet))
    printing_out = asyncio.create_task(printout_slots(final_lines))
    winnings: int = await checking_winnings
    await printing_out
    return winnings
    

## Spin the slots
async def spin_slots(num_lines: int, bet: int) -> int:
    all_symbols: list[str] = get_all_symbols(symbol_counts)
    drawn_collumns: list[list[str]] = draw_random_symbols(ROWS, COLLUMNS, all_symbols)
    final_lines: list[list[str]] = reorder_collums(drawn_collumns)
    winnings: int = await spin_user_animation(final_lines, num_lines, bet)
    return winnings


# INPUT
## Error Handling
def is_valid_number(string_input: str) -> bool:
    if string_input.isdigit():
        return True
    
    print("Please enter a valid number")
    return False
    
## User Values
def get_deposit() -> int:
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

def get_number_of_lines() -> int:
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

def get_bet() -> int:
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

## Main Input
def get_input() -> tuple():
    bet: int = 0
    balance: int = get_deposit()
    num_lines: int = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet: int = bet * num_lines
        if total_bet > balance:
            print(f"Your bet of ${total_bet} is more than your balance of ${balance}")
            continue

        break

    print(f"You are betting ${bet} on {num_lines}. Total bet is: ${total_bet}")

    return (num_lines, bet)


# PROGRAM START
async def start() -> None:
    num_lines, bet = get_input()
    winnings = await spin_slots(num_lines, bet)
    
    print(f"You've won ${winnings}!")
    

asyncio.run(start())