import random
ls = [1,2,3,4,5,6,7,8,9,0]
(random.shuffle(ls))
print(ls)

lst = [3,6,7,8]
seed = 7
random.Random(seed).shuffle(lst)
print(lst)

