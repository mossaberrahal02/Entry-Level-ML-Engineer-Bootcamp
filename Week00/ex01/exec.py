import sys


j = len(sys.argv) - 1
while j > 0:
    i = len(sys.argv[j]) - 1
    while i >= 0 :
        if sys.argv[j][i].islower():
            print(sys.argv[j][i].upper(), end='')
        if sys.argv[j][i].isupper():
            print(sys.argv[j][i].lower(), end='')
        i-=1
    j-=1
    if j > 0: print(" ", end='')
if len(sys.argv) - 1 > 0:
    print("")
