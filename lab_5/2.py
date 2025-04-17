with open('lab_5\input2.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f.readlines()]

sorted_numbers = sorted(numbers)

with open('lab_5\output2.txt', 'w') as f:
    for num in sorted_numbers:
        f.write(f"{num}\n")
