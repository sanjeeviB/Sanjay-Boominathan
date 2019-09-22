#Q 17  Write a program that computes the net amount of a bank account
# #based a transaction log from console input. The transaction log format is shown as
    # D 100
    # W 200

total = 0
while True:
    a = input("ENTER THE AMOUNT ").split()
    if  not a:
        break
    cm,num=map(str,a)
    if cm=='D' or cm=='d':
        total+=int(num)
        print("DEPOSIT : ",total)
    if cm=="W" or cm=='w':
        total-=int(num)
        print("WITHDRAWAL : ", total)
    print("---",total,"---")
print("BALANCE AMOUNT : ",total)