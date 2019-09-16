#factorial  EXAMPLE 8*7*6*5*4*3*2*1
#INPUT program: 8
#OUTPUT 40320

n = int(input("ENTER THE NUMBER:")) #input() function takes input as string type
                     #int() converts it to integer type
fact = 1
i = 1
while i <= n:
    fact = fact * i;
    #print(i)
    #print(fact)
    i = i + 1
    #print(fact)

print(fact)