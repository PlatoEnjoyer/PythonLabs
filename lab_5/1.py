with open('lab_5\input1.txt', 'r') as f:
    numbers = list(map(int, f.read().split()))
    
product = 1
for num in numbers:
    product *= num

with open('lab_5\output1.txt', 'w') as f:
    f.write(str(product))
