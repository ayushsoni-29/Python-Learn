my_list = [23, 433, 2378, 346]

max = my_list[0]

sec = my_list[0]

for i in range(len(my_list)):
    if my_list[i] > max:
        max = my_list[i]

for i in range(len(my_list)):
    if my_list[i] > sec and my_list[i] != max:
        sec = my_list[i]

print(sec)