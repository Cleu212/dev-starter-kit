print("Unit Converter")
print("1 - Kilometers to Meters")
print("2 - Meters to Kilometers")
print("3 - Kilograms to Grams")
print("4 - Grams to Kilograms")

choice = input("Choose an option (1-4): ")

value = float(input("Enter the value: "))

if choice == "1":
    print("Result:", value * 1000, "meters")
elif choice == "2":
    print("Result:", value / 1000, "kilometers")
elif choice == "3":
    print("Result:", value * 1000, "grams")
elif choice == "4":
    print("Result:", value / 1000, "kilograms")
else:
    print("Invalid option")
