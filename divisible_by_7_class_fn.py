#Q 20
#Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

class Test:
    def gen(self,n):
        return[i for i in range(n) if(i%7==0)]

n=int(input("ENTER THE NUMBER: "))
num = Test()
print (num.gen(n))