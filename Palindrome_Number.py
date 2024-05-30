org = 3553

rev = 0

tem = org

while org > 0:
    last_dig = org % 10
    rev = rev * 10 + last_dig
    org = org//10

if tem == rev:
    print("is palindrome")
else:
    print("is not palindrome")