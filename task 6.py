positions = int(input("Enter number of positions to fullfill:  "))
my_list = []
for i in range(0, positions, 1):
    key = ["name", "price", "quantity"]
    input_value = input("Enter item name, price, quantity separated by space: ")
    value = input_value.split()
    i = dict(zip(key, value))
    my_list.append(i)
    print(i)
for number, list in enumerate(my_list, 1):
    print(number, list)
