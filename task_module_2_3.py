my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
b = []
while a < len(my_list):
    if my_list[a] < 0:
        break
    if my_list[a] > 0:
        b.append(my_list[a])
    a += 1
print(b)

