def reverse(x):
    return x[::-1]

string=input("Enter a String : ")
temp=reverse(string)
if(string==temp):
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
