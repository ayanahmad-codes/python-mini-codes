a = "Python !!! This is a string method. !!!!!! ayan !! ahmad !! ayan !! ayan"


print(len(a))
print(a.upper())
print(a.lower())
print(a.title())
print(a.rstrip("!"))
print(a.replace("string", "replace"))
print(a.replace("meth", "mo"))
print(a.split(" ")) # list bana deta h
print(a.split(",")) # comma laga ke list bana dega
print(a.capitalize())#first letter on / agar capital hai to small ho jayega/

print(a.endswith("!!!"))
print(a.count("ayan"))
print(a.find("ayan"))
print(a.find("power")) # agar string me exist nhi krta hai to -1 milega
# print(a.index("power")) # agar exist nhi krta h to error dega / similar h dono find or index


# is True or false dega

print(a.isalnum()) # 0-9 or A - z or a-z tab true dega
print(a.isalpha()) # only alphabets hoga string tab true dega
print(a.isupper())
print(a.islower())
print(a.isspace()) # white hoga to true dega
print(a.istitle())
print(a.startswith("python"))
print(a.swapcase()) # yh upper ko lower or lower ko upper karta hai pure string ko.

b = "lion with cat/n" # /n print nhi hota h is liye false dega
print(b.isprintable())


str = "Welcome to console python boss 123!"
print(len(str))
print(len(str.center(31))) # not working
print(str.count("o"))
print(str.endswith("!"))
print(str.isalnum())
print(str.isprintable())
 




