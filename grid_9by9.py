import random
final_list=list()
for i in range(9):
    list1 = list()
    while len(list1) < 6:
        num = random.randrange(1, 7, 1)
        if num not in list1:
            list1.append(num)
    list2 = list()
    while len(list2) < 3:
        num = random.randrange(1, 7, 1)
        if num not in list2:
                list2.append(num)

    final_list.append(list1+list2)


print(len(final_list), len(final_list[0]))
print("[")
for i in range(len(final_list)):
    print(f"    {final_list[i]},")
print("]")

