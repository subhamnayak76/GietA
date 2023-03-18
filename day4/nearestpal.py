#nearest panlindrome in of number
#99 -> 101
#1221 -> 1331
n = int(input())

def nearest_palindrome(n):
    flag = 0
    while flag != 1:
        n= n+1
        s = " "
        s = str(n)
        if s == s[::-1]:
            flag = 1
            return s




print(nearest_palindrome(n))