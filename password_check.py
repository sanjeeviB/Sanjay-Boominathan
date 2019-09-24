#Q 18    password check
# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# At least 1 character from [&]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# input -- ABd1234@1,a F1#,2w3E*,2We3345
# output -- ABd1234@1

count=0
def check(x):
    #count=(len(x)>=6 and len(x)<=12)
    count= (6<=len(x) and len(x)<=12)
    #print(count)
    for a in x:
        if a.isupper():
            count+=1
            print("upper",count)
            break
    for a in x:
        if a.islower():
            count+=1
            print("lower",count)
            break
    for a in x:
        #if a.isnumberic():
        if '0' <= a and a <= '9':
            count+=1
            print("num",count)
            break
    for a in x:
        if(a=="@" or a=="$" or a=="#" or a=="&"):
            count+=1
            print("$#@&",count)
            break
    print("total",count)
    return count>=5

password = str(input("ENTER THE PASSWORD TO CHECK : "))  #.split(',')
lst = check(password)
#lst = filter(check,password)
print("RESULT :",lst)
print(password)