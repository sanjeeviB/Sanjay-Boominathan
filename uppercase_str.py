from typing import List

string = []
#print ("-----",string,"-----")

while True:
    x = input("ENTER THE STRING : ")
    if len(x) == 0:
        #print("ENTER THE STRING ")
        break;
    string.append(x)

    #print (string)
str(string)
print(type(string))

for line in string:
    print(line.upper())