word = input("ENTER THE STRING: ").split()

word.sort()
print(word)

for i in word:
    if word.count(i) > 1:
        word.remove(i)
        print(word)

print(" ".join(word))