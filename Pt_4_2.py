def palindrome(x):
    arr = []
    for i in range(0, len(x)):
        for j in range(i + 1, len(x) + 1):
            s = x[i:j]
            if s == s[::-1] and len(s) > 1 and not (" " in s):
                arr.append(s)
    return arr


print(palindrome(input("Найти палиндромы в строке ")))
