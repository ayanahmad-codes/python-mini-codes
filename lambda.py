m = float(input())      # Input mass
v = float(input())      # Input velocity

momentum = lambda m, v: m * v   # Lambda function to calculate momentum
result = momentum (m, v), 2) 
print(result)

n = int(input())          # Take integer input
r = lambda x: x * 5       # Define lambda function to multiply by 5
print(r(n))               # Call lambda function and print result

words = ["apple", "banana", "cherry"]
words.sort(key=lambda w: w[-1])
print(words)  # Output: ['banana', 'apple', 'cherry']

nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Output: [1, 4, 9, 16, 25]

add_ten = lambda x: x + 10
print(add_ten(5))   # Output: 15


maximum = lambda a, b: a if a > b else b
print(maximum(10, 15))  # Output: 15
