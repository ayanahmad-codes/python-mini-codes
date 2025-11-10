def greet():
    name = "Ayan"  # local variable
    print("Hello", name)

greet()
print(name)  # ❌ Error: name is not defined

Hello Ayan
NameError: name is not defined

x = 10  # global variable

def show():
    print("Inside function:", x)

show()
print("Outside function:", x)

count = 0  # global variable

def increment():
    global count
    count += 1
    print("Inside function:", count)

increment()
print("Outside function:", count)

x = 5

def change():
    x += 1   # ❌ Error: UnboundLocalError
    print(x)

change()


def increment(x):
    return x + 1

count = 0
count = increment(count)
print(count)
