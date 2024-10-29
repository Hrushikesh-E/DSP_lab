input_list = []
e = int(input("Enter length: "))

for l in range(e):
    number = input("Enter a number: ")
    input_list.append(number)

output = [] 

accumulator = 0

for i in input_list:
    if i.lower() == 'exit': 
        break
    try:
        n = float(i)
        accumulator += n
        output.append(f"Accumulator value: {accumulator}")
    except ValueError:
        output.append("Invalid input. Please enter a valid number.")

output.append(f"Final accumulator value: {accumulator}")

for k in output:
    print(k)
