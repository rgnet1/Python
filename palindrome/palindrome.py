# Palindrome is a string that can read forwards and backwards

# Write a function that detects a Plindrome

def isPalindrom(string):
    left = 0
    right = len(string) -1
    while(right >= left):
        if string[left] != string[right]:
            return 0
        left +=1
        right -=1
    return 1

print(isPalindrom("racecar"))
print(isPalindrom("cc."))


def Paindrom()