given_list = [i for i in range(1, 101) if i != 42]  # Suppose 42 is missing
missing_number = sum(range(1, 101)) - sum(given_list)
print("The missing number is:", missing_number)
