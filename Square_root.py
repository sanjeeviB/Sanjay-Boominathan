# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.


from  math import *
C = 50
H = 30
i = ""
def cal(D):
    return sqrt((2*C*D)/H)

D = input("ENTER THE INPUT VALUE: ").split(",")
D = [int(i) for i in D]
#print (i)
print (D)
D = [cal(i) for i in D]
print (D)
D = [round(i) for i in D]
print (D)
#print (i)
for i in D:
    print(i)
D = [str(i) for i in D]
print (D)
#print (i)

print (",".join(D))
print ("|".join(D))