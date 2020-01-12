my_list = [7, 5, 3, 3, 2]

while True:
    number = int(input("Enter rating number: "))
    my_list.append(number)
    print(sorted(my_list))
    first_line = sorted(my_list)
    first_line.reverse()
    print(first_line)

