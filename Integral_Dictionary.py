#Integral_Dictionary
#INPUT  5
#OUTPUT {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


n = int(input("ENTER THE NUMBER"))
ans = {}
print (ans)
for i in range (1,n+1):
    ans[i] = i * i
    #print(i)
    #print(ans)
    #print(ans[i])
print(ans)