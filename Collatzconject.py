n = int(input("Please enter a number other than 0: "))

if n < 1:
    print("Use a positive integer")
    exit()

steps = 0

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(n)
    steps += 1

print("Total number of steps: ", steps)