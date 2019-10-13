#q 27
# Define a function that can convert a integer into a string and print it in console.

def PrintValue(n):
    print(str(n))

PrintValue(input("ENTER THE VALUE "))


conv= lambda a : str(a)
n=conv(input("enter the number or value"))
print(n)
print(type(n))