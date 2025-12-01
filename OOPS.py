# class Car:
#     def __init__(self, brand, model, numberplate):

#         self.brand = brand
#         self.model = model
#         self.numberplate = numberplate

#     def full_name(self):
#         print("My dream car is", self.brand, self.model)
#         return f"My dream car is {self.brand} {self.model}"
       


# first_car = Car("Buggati", "chiron", 7777)
# print(first_car.full_name())
# print(first_car.brand) 
# print(first_car.model) 
# print(first_car.numberplate)

class Dream_car:
    def __init__(self, brand, model):

      
        self.brand = brand
        self.model = model
        

    def car(self):
        print(f"your first car is {self.brand} {self.model}")
    
class Electric_car(Dream_car):

    def __init__(self, brand, model, battery_size):

        super().__init__(brand, model)

        self.battery_size = battery_size

my_car = Electric_car("Toyota", "corolla", "90Kwh")

my_car.car()




# print(my_car.car())
# print(my_car.brand)
# print(my_car.modern)

       


























# class Student:
#     name = "ayan"
#     roll_num = 22
#     section = "k25rm"
#     date = 11

# obj = Student()
# print(obj.name)
# print(obj.roll_num)
# print(obj.section)
# print(obj.date)

# class Laptop:
#     company = "HP"
#     model_no = "victus"
#     product_no = "f2v23w"
#     serial_no = "23456"

# laptop = Laptop()
# print(laptop.company)
# print(laptop.model_no)
# print(laptop.product_no)
# print(laptop.serial_no)


# class Name:
     
#      firstname = "Ayan"

#      def __init__(self, age, marks, cost):
        
#          self.age = age
#          self.marks = marks
#          self.cost = cost

# details = Name("age", "marks", "cost")

# print(details.age)
# print(details.marks)
# print(details.cost)

# Name.firstname = "Sarika ahmad"
# print(details.firstname)


# # create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print average.

# class Details:

#     def __init__(self, name, marks):

#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name,"your average score is:", self.marks )

# s1 = Details("Thor", [88, 99, 95])
# s1.get_avg()


# class Account:

#     def __init__(self, bal, acc):

#         self.balance = bal
#         self.account_no = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debitted")
#         print("total balance =", self.balance, )

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs ", amount, "was credited")
#         print("total balance =", self.get_balance())

#     def get_balance(self):
#             return self.balance
# acc1 = Account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(350)
