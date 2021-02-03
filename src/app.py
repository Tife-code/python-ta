import sys
import os


def palindrome(s):
    global check
    check =[]
    for char in s:
        check.append(char)
        if char == " ":
            check.remove(" ")
    palindrome=check[::-1]
    if palindrome == check:
        return True
    else:
        return False
   
    

def solution(s):
    return palindrome(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argment required"))

    print(solution(sys.argv[1]))


