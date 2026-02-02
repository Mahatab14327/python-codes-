print("Welcome to Feet to Meters And Meters to Feet Converter!")

choice = input("Type '1' to convert Feet to Meters or '2' to convert Meters to Feet: ")
if choice == "1":
 feet = float(input("Enter the value in Feet:"))
 print("Meters:",round(feet/3.28, 3))
else:
 meters = float(input("Enter the value in Meters:"))
 print("Feet:",round(meters*3.28, 3))
