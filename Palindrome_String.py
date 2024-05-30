num = "abcdcba"

start = 0
end = len(num) - 1
mid = (len(num)-1)//2
flag =0

while (start<mid):
    if num[start] == num[end]:
        start = start + 1
        end = end - 1
    else:
        flag = 1
        break

if flag==1:
    print("num is not palindrome")
else:
    print("num is palindrome")