import itertools
import csv

# Define the possible operations
operations = ['+', '-', '*']

# Get input for the range of N and K values
min_N = int(input("Enter the minimum value for N: "))
max_N = int(input("Enter the maximum value for N: "))
min_K = int(input("Enter the minimum value for K: "))
max_K = int(input("Enter the maximum value for K: "))

# Initialize a counter for the number of calculations
cnt = 0

# Open a CSV file to record the results
with open('matching_cases.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['A', 'B', 'Result', 'Matching Equation'])

    # Iterate over all values of N (A values) and K (B values) within the specified range
    for A_initial in range(min_N, max_N + 1):
        for B in range(min_K, max_K + 1):
            # Pre-calculate the special case result for this A_initial and B
            special_case_result = eval(f"(({A_initial} + {B}) * {B}) - 5")

            # Iterate through all combinations of operations
            for op1, op2, op3 in itertools.product(operations, repeat=3):
                try:
                    # Calculate A and C based on the current operations
                    A = eval(f"({A_initial} {op1} {B}) {op2} {B}")
                    C = eval(f"{A} {op3} 5")
                    cnt += 1

                    # Check if the current operation combination is the special case
                    if op1 == '+' and op2 == '*' and op3 == '-':
                        # Print the special case (for reference), but don't compare it to itself
                        print(
                            f"\033[91mA = ({A_initial} {op1} {B}) {op2} {B} = {A}")
                        print(f"C = {A} {op3} 5 = {C}\033[0m")
                    else:
                        # Compare with the special case result
                        print(f"A = ({A_initial} {op1} {B}) {op2} {B} = {A}")
                        print(f"C = {A} {op3} 5 = {C}")

                        if C == special_case_result:
                            writer.writerow(
                                [A_initial, B, C, f"({A_initial} {op1} {B}) {op2} {B} {op3} 5"])
                            print(
                                f"Identical result found for A={A_initial}, B={B}, Result={C} with equation: ({A_initial} {op1} {B}) {op2} {B} {op3} 5")
                            print('------')
                            break  # Stop current iteration if identical result is found

                    print('------')

                except ZeroDivisionError:
                    print(
                        f"Skipping division by zero for operations: {op1}, {op2}, {op3}")
                    print('------')

# Print the total number of calculations performed
print(f"Total number of calculations: {cnt}")
