# Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.

#x=[]
str = input("ENTER THE ARRAY[STR] :").split(",")
str.sort()
#str.upper()
abc = (",".join(str))
print("LOWERCASE: ",abc)
print("UPPERCASE: ",abc.upper())
