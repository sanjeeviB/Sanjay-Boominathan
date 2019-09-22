
upper =0
lower =0

word=input("ENTER THE STRING TO FIND THE COUNT OF LOWER & UPPER  CASE : ")

for i in word:
    if("a"<=i and "z">=i):
        lower+=1
    if("A"<=i and "Z">=i):
         upper+=1

print("LOWER:{0}\nUPPER:{1}".format(lower,upper))
print("LOWER %d\nUPPER %d"%(lower,upper))

print("LOWER CASE COUNT : {0}\nUPPER CASE COUNT : {1}".format(lower,upper))
