numbers = [4, 3]
x = min(numbers)
y = max(numbers)

counter = 1
while y != x:
    y = y - x
    numbers = [x, y]
    x = min(numbers)
    y = max(numbers)

    counter = counter + 1
        
print(counter)

# from functools import reduce

# numbers = [

#     input(),

#     input()

# ]

# result = reduce(lambda x, y: x + y, map(lambda i: int(i), numbers))

# print(result)