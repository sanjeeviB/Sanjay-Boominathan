import sys
print("sys.version : ",sys.version)
print("sys.version_info : ",sys.version_info)

# it's easy to print this list of course:
print(sys.argv)

# or it can be iterated via a for loop:

for i in range(len(sys.argv)):
    if i == 0:
        print("Function name: %s" % sys.argv[0])
    else:
        print("%d. argument: %s" % (i,sys.argv[i]))

for i in (sys.stdin, sys.stdout, sys.stderr):
    print(i)
