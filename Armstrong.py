num = 153
arm = 0
temp = num

length = str(num)

while num>0:
    last = num%10
    arm = arm + (last**len(length))
    num = num//10

if arm == temp:
    print("num is armstrong")
else:
    print("not armstrong")
