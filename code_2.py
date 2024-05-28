temp=float(input("Enter temperature value: "))
unit=input("Enter the unit you have inputed now (C or F): ").upper()
if unit == "C":
  far=(temp * 1.8) + 32
  print("The Fahrenheit value is : ",far)
else:
  cel=(temp - 32) / 1.8
  print("The Celsius value is : ",cel)
