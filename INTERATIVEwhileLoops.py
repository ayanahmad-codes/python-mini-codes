#while loops
i = 1
while i <= 10:
    print("i am learning python", i) # This will print infinite times
    i += 1 # i += 1 is same as i = i + 1
    print("loop finished")
i = 1
while i <= 1000:
    print("i am learning coding", i) 
    i += 1

i= 1
while i <= 100:
    print(i)
    i += 1
i = 100
while i >= 1:
    print(i)
    i -= 1

i = 1 # print first 10 multiples of 3
while i <= 10:
    print(3*i)
    i += 1


nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0 
while idx < len(nums):
    print(nums[idx])
    idx += 1
 
heroes = ["ironman", "thoer", "spiderman", "hulk", "captain america"]
i = 0
while i < len(heroes):
    print(heroes[i])
    i += 1
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at index", i)
    i += 1

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for el in nums: # for loop
    print(el)

nums = (1, 2, 3, 4, 5, 56, 67, 78, 89, 100)
x = 5
idx = 0
for el in nums:
    if(el == x):
        print("number found at idx", idx)
        idx += 1

i = 1
while i <= 5:
    print(i)
    if(i == 4):
        break
    i += 1
    print("loop ended")
i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)  #skip
    i += 1


list = [1, 3, 4, 5, 6, 7, 9, 10]
for val in list:
    print(val)

str1 = ["ayan", "ali", "reza", "lucky", "hasan"] 
for val in str1:
    print(val)  
tup = (1, 2, 3, 4, 5,)
for num in tup:
    print(num)


str2 = "lovelyprofessional"


for character in str2:  # short char
    print(character)

nums = [1, 22, 55, 66,  78, 45, 66 ]
x = 66
i = 0
for nums in nums:
    if(nums == x):
        print("number found at index : ", i)
        i += 1


    seq = range(10)
    for i in seq:
        print(i)

    # for i in range(15):    # range bina variable k bhi use kr skty hn
    #     print(i)

    # for i in range(5, 15):
    #     print(i)

    # for i in range(1, 10, 2): odd numbers
    #     print(i)    

# for i in range(10, 0, -1):
#     print(i)


# for i in range(2, 50, 2):
#     print(i) # even numbers

# for i in range(1, 101):
#     print(i)

# for i in range(100, 0, -1):
#     print(i)  

# num = int(input("enter a number: "))
# for i in range(1, 11):
#     # print(num, "x", i, "=", num*i)
#     print(f"{num} * {i} = {num*i}")

# pass statement
for i in range(5):
    pass
# print("python isko samjhta hai ki loop complete hua")


n = int(input("enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
    print("sum is: ", sum)
print("final sum is: ", sum)


num = 5
i = 1
sum = 0
while i <= num:
    sum += i
    i += 1
    print("final sum is: ", sum)
print("final sum is: ", sum)

# factorial of a number suppposed mujhe 5 ka factorial nikalna hai 5! = 1*2*3*4*5 = 120
# 1 * 6 * 24 * 120 yeh factorial ka logic hai
num = 5
i = 1
fact = 1
while i <= num:
    fact *= i
    i += 1
    print("factorial is: ", fact)

print("final factorial is: ", fact)
# final factorial ke liye print loop k bahar krna hai!
# same factorial for loop se
n = 7
fact = 1
for i in range(1, n+1):
    fact *= i
    print("factorial is: ", fact)

print("final factorial is: ", fact)

