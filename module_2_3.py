my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
counter = -1
while counter < len(my_list):
    counter = counter + 1
    if my_list[counter] < 0:
        break
    if my_list[counter] == 0:
        continue
    if my_list[counter] > 0:
        print(my_list[counter])








