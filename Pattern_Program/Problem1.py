number = int(input("Enter the Number : "))

for line in range(1, number + 1):
    for column in range(line):
        print("*", end = "")
    print()