#Q 19
#
# You are required to write a program to sort the (name, age, score) tuples by ascending order
# where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:
#
# 1: Sort based on name
# 2: Then sort based on age
# 3: Then sort by score

lst=[]   # using list and appending to  tuple
while True:
    a=input("ENTER THE NAME , AGE , SCORE WITH "+":").split(",")
    if not a[0]:
       break
    lst.append(tuple(a))
    #lst.sort(key= lambda a:(a[0]))
    lst.sort(key= lambda a:(a[0],a[1],a[2]))
print(lst)