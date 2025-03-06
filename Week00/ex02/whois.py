import sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
    exit(1)
elif len(sys.argv) == 1:
    exit(0)

if sys.argv[1].isdigit() == 0:
    print("AssertionError: argument is not an integer")
    exit(1)

def myAtoi(str):
    i = 0
    result = 0
    # s = 1
    # if str[i] == '-':
    #     s = -1
    #     i+=1
    for i in range(0, len(str)):
        result = result * 10 + (ord(str[i]) - 48)
        i+=1
    return result
num = myAtoi(sys.argv[1])
if num == 0:
    print("I'm Zero")
elif num % 2 == 0:
    print("I'm Even")
else:
    print("I'm Odd")
