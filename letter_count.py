#program that accepts a sentence and calculate the number of letters and digits.

letter =0
digit =0
special = 0
word = input("ENTER THE STRING TO FIND COUNT IN IT : ")

for i in word:
    #if("a">=i and 'z'<=i) or (i>='A' and i<='Z'):
    if(i>="a" and i<='z') or (i>='A' and i<='Z'):
        letter+=1
    if i>='0' and i<='9':
        digit+=1
    # else:
    #      special+=1

print("LETTERS:{0}\nDIGITS:{1}".format(letter,digit))
print("LETTERS %d\nDIGITS %d"%(letter,digit))

print("LETTER COUNT : {0}\nDIGIT COUNT : {1}".format(letter,digit))

# print("LETTERS:{0}\nDIGITS:{1}\nSPECIAL:{2}".format(letter,digit,special))
# print("LETTERS %d\nDIGITS %d\nSPECIAL %d"%(letter,digit,special))

# print("LETTER COUNT : {0}\nDIGIT COUNT : {1}\nSPECIAL COUNT : {2}".format(letter,digit,special))
