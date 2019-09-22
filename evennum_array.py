#Q.16 Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.

a = input("ENTER THE ARRAY TO FIND EVEN NUM INIT : ").split(",")
#print(a)
lst=[]
for i in a:
    if(int(i)%2):
        print(",".join(i))
        lst.append(i)
        #print(",".join(lst))
print(",".join(lst))
print("____")