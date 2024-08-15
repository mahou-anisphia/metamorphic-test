import itertools

# Define the possible operations
operations = ['+', '-', '*', '/']

# Define the values for A and B
A_initial = 1  # You can change this value as needed
B = 2  # You can change this value as needed
cnt = 0
# Iterate through all combinations of operations
for op1, op2, op3 in itertools.product(operations, repeat=3):
    try:
        # Calculate A and C based on the operations
        A = eval(f"({A_initial} {op1} {B}) {op2} {B}")
        C = eval(f"{A} {op3} 5")
        cnt += 1

        # Check for the specific case
        if op1 == '+' and op2 == '*' and op3 == '-':
            print(f"\033[91mA = ({A_initial} {op1} {B}) {op2} {B} = {A}")
            print(f"C = {A} {op3} 5 = {C}\033[0m")
        else:
            print(f"A = ({A_initial} {op1} {B}) {op2} {B} = {A}")
            print(f"C = {A} {op3} 5 = {C}")
        print('------')

    except ZeroDivisionError:
        print(f"Skipping division by zero for operations: {op1} and {op2}")
        print('------')
print(f"Number of calculation: {cnt}")
