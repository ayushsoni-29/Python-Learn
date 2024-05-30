my_list = [1,3,4,4,5,7,9,9]

temp = []

for x in my_list:
    if x not in temp:
        temp.append(x)

print(temp)
