#function definition
# def calculate_sum(a, b): # a, b ko parameters kehte h
#     return a + b

# #function call jab variable me store krte h def ke baad wale ko!
# results = calculate_sum(5, 15) # 5, 15 arguments kehte h or yahi values parameters me jate h
# print(results)

# def avg_marks(marks1, marks2, marks3):
#     sum = marks1 + marks2 + marks3
#     average = sum / 3
#     return average

# student_average = avg_marks(70, 80, 60)

# def cal_prod(a , b=2): # b ka default value 2 h
#     return a * b
# cal_prod(2)
# print(cal_prod(2))
# print(cal_prod(2, 3))



states = ["rajasthan", "bihar", "himachal", "punjab"]
countries = ["india", "usa", "uk", "germany"]
# def print_len(list):
#     print(len(list))

# print_len(states)
# print_len(countries)

# def print_list(list):
#     for items in list:
#         print(items, end=" ") # end=" " se sab ek line me print hote h
#     print() # new line ke liye
# print_list(states)

# print_list(countries)
# pass
# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#         print(fact)
        
# cal_fact(6)


# print("final factorial is: ", )


def converter(usd_val):
    inr_val = usd_val * 82
    print("INR value is: ", inr_val)
    return inr_val
print(converter(9))

def num_check(num):
    x = int(input())
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"
y = num_check(5)
print(y)




