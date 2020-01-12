month = int(input("Enter number: "))

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

new_month = month -1

print(months[new_month])

if new_month < 2:
    print("List says: Winter")
elif new_month >=2 and new_month <5:
    print("List says: Spring")
elif new_month >=5 and new_month <8:
    print("List says: Summer")
elif new_month >=8 and new_month <11:
    print("List says: Autumn")
else:
    print("List says: Winter")

time_of_year = {1 : "Winter", 2 : "Winter", 3 : "Spring", 4 : "Spring", 5 : "Spring", 6 : "Summer", 7 : "Summer", 8 : "Summer", 9 : "Autumn", 10 : "Autumn", 11 : "Autumn", 12 : "Winter"}
print("Dictionary says: ", time_of_year[month])