#q.15 Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# N*a=Na

a = (input("ENTER THE NUM: "))
total =int(a) + int(2*a) + int(3*a) + int(4*a)
print(int(a))
print(int(2*a))
print(int(3*a))
print(int(4*a))
print(total)


# a = input()
# total,tmp = 0,str()        # initialing an integer and empty string
#
# for i in range(4):
#     tmp+=a               # concatenating 'a' to 'tmp'
#     total+=int(tmp)      # converting string type to integer type
#
# print(total)
