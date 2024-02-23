N = 1344
reversed_N = 0
while N >0:
    digit = N % 10
    reversed_N = reversed_N * 10 + digit
    N = N // 10
    print("Reversed number:", reversed_N)

