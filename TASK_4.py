a= int(input("Enter the first number:"))
b= int(input("Enter the second number:"))
c= (input("Enter the Arethmatic operator:"))
if(c=='+'):
  print(a+b)
elif(c=='-'):
  print(a-b)
elif(c=='*'):
  print(a*b)
elif(c=='/'):
  print(a/b)
elif(c=='%'):
  print(a%b)
else:
  print("Invalid operator")
