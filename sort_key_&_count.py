#Q 22
#Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# input : New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
#output :
        # 2:2 3.:1 3?:1
        # New:1 Python:5 Read:1
        # and:1 between:1
        # choosing:1 or:2 to:1

a = input("ENTER THE WORDS: ").split()
word = sorted(set(a))
print(word)
for i in word:
    print("{0}:{1}".format(i, word.count(i)))
