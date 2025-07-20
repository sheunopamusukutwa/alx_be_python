number_input = input("Enter a number to see its multiplication table: ")

if number_input.strip().lstrip('-').isdigit():
    number = int(number_input)

    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")
else:
    print("Invalid input. Please enter a valid integer.")