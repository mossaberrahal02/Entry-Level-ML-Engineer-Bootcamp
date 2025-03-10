# def text_analyzer(text):
#     """ this is the documentation of this function """
#     while not text:
#         text = input("enter the string")
#     if not isinstance(text, str):
#         print("not a string")
#         exit(1)
#     totalNumberOfCharacters = len(text)
#     uperCaseCount = 0
#     lowerCaseCount = 0
#     ponctualCharacter = 0
#     space = 0
#     for i in range(0, len(text)):
#         if text[i].isupper():
#             uperCaseCount += 1
#         elif text[i].islower():
#             lowerCaseCount += 1
#         elif text[i] == ' ':
#             space += 1
#         else:
#             ponctualCharacter += 1
#     print("totalNumberOfCharacters = ", totalNumberOfCharacters)
#     print("uperCaseCount = ", uperCaseCount)
#     print("lowerCaseCount = ", lowerCaseCount)
#     print("space = ", space)
#     print("ponctualCharacter = ", ponctualCharacter)

# text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")
# print("__doc__ == ", text_analyzer.__doc__)

import sys

def text_analyzer(text):
    """ this is the documentation of this function """
    while not text:
        text = input("enter the string")
    if not isinstance(text, str):
        print("not a string")
        exit(1)
    totalNumberOfCharacters = len(text)
    uperCaseCount = 0
    lowerCaseCount = 0
    ponctualCharacter = 0
    space = 0
    for i in range(0, len(text)):
        if text[i].isupper():
            uperCaseCount += 1
        elif text[i].islower():
            lowerCaseCount += 1
        elif text[i] == ' ':
            space += 1
        else:
            ponctualCharacter += 1
    print("totalNumberOfCharacters = ", totalNumberOfCharacters)
    print("uperCaseCount = ", uperCaseCount)
    print("lowerCaseCount = ", lowerCaseCount)
    print("space = ", space)
    print("ponctualCharacter = ", ponctualCharacter)
if __name__=="__main__":
    if len(sys.argv) != 2:
        print("bad number of arguments")
        exit(1)
    text_analyzer(sys.argv[1])