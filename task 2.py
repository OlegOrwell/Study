input_list = input("Enter a list numbers or elements separated by space: ")
list_1 = input_list.split()
print("user list is ", list_1)
length = len(list_1)

for i in range(0, length-1, 2):
    list_1[i], list_1[i+1] = list_1[i+1], list_1[i]

print(list_1)

