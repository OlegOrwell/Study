input_list = input("Enter a list numbers or elements separated by space: ")
list_1 = input_list.split()
print("user list is ", list_1)

length = len(list_1)

for i in range(0, length, 1):
    print(list_1[i])

for number, list in enumerate(list_1, 1):
    print(number, list[:10])