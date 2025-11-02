str1 = 'Hello Alice'
str2 = "This is a python lecture"
str3 = '''I am learing python.'''
str4 = """Python is a game changer."""
str5 = '''He said, "I'm learing python.'''
str5 = "He said.\ni'm want to become a coder." # /n is used for new lineS
# print(str1)
# print(str2)
# print(str3)
# print(str4)
# print(str5)
#concatenation
first = "Ayan"
last = "coder"
#print(first + last)
#print(first + "" + last) # "is used to add space"
len2 = len(str2) # length counter in digits
#print(len2)
#print(str2[0]) # indexing start from 0
name = "python guru"
#print(name[7]) # space is also a character


str6 = "i am a good coder" # slicing
#print(str6[0 : 5])
#print(str6[0 : 11])

str7 = " i am studying pthon from Apna college"
#print(str7.endswith("college")) # it will return true or false
#print(str7.capitalize()) # it will capitalize the first letter of the string

str8 = "i want to become a cool x coder"
#print(str8.replace("cool x", "good")) #it will replace the word
str9 = "he is a better teacher than him"
#print(str9.find("teacher")) # it will return the index of the word.
str10 = "we are learning python programming language" 
#print(str10.count("a")) # it will count the number of times the letter is present in the string 


# Test

#Name1 = input("enter name :")
#print("welcome", Name1,"to the world of python programming language.","we are happy to have you here")
#print("length of your Name1 is", len(Name1))

string22 = "Hello everyone ,/nI am $ the very expensive $99.89."
#print(string22.count("$"))


age = 20
if(age >= 18): #condition  
    #print("you can vote")
    pass

    #condition statements

    #light = "green"

    #if(light == "red"):
    #     print("you cannot cross the road")
    #if(light == "yellow"):
    #    print("you cannot cross the road")
    #if(light == "green"):
        #print("you can cross the road")
    
    # light = "red"
    # if(light == "green"):# if condition is wrong it will check the next condition
    #     print("you can cross the road")
    # elif(light == "yellw"):
    #     print("you should get ready to cross the road")
    # elif(light == "red"):
    #     print("you cannot cross the road")
    
    # num = 10
    # if(num > 50):
    #     print("num is greater than 50")
    # elif(num > 5):
    #      print("num is less than 50 but greater than 5")

light = "green"
# if(light == "red"):
#         print("you cannot cross the road")
# elif(light == "yellow"):
#        print("you shuld get ready to cross the road")
# else:
#        print("you can cross the road")
    
#marks = int(input("enter student marks :"))
# if(marks >= 90):
#     print("A grade")
# elif(marks >= 80 and marks < 90):
#     print("B grade")
# elif(marks >= 70 and marks > 80):
#     print("C grade")
# elif(marks >= 60 and marks > 50):
#     print("D grade")
# else:
#     print("grade of the student is, grade")



# num = int((input("enter a number :")))
# if(num % 2 == 0):
#     print("even number")
# else:
#     print("odd number")

age = 95
# nesting of if wth if
if(age >= 18):
    if(age >= 70):
        print("you cannot drive")
    else:
        print("you can drive 2 wheeler and 4 wheeler")
else:
    print("you cannot drive")