while True:
    size_entered = input("Enter the size of the pattern: ")
    if size_entered.isdigit() and int(size_entered) > 0:
        size = int(size_entered)
        break
    else:
        print("Invalid input. Please enter a positive integer.")

row = 0
while row < size:
    for column in range(size):
        print("*", end="")
    print()
    row += 1