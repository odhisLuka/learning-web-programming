from urllib.parse import parse_qs

name = input("Name: ")
# what this code does is it prompts the user to type in their name and save it in a variable calle name

print("Hello, " + name)
#this code retuns hello, name when the user types in their name

#alternatively, you can use fstr, also called formatted string, to substitute the value of the variable
print(f"Hello, {name}")
