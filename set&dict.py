my_dict = {
    "name" : "a small animal",
    "table" : "a piece of furniture",}

print(my_dict['name'])
print(my_dict['table'])


subjects = {"python", "java", "c++", "c", "javascript", "python"}
print(subjects)


list = ["ayan", "566", "kishanganj"]
print(list)
list[0] = "serial"
print(list)
list[2] = "killer"
print(list)

list2 = [88, 77, 99, 67, 55, 45]
print(list2[1:4])
print(list2[:3])  #same as 0:3
print(list2[0:3])

marks = {}

x = int(input("enter phy :"))
marks.update({"phy" : x})
x = int(input("enter che :"))
marks.update({"che": x})
x = int(input("enter math :"))
marks.update({"math" : x})
print(marks)