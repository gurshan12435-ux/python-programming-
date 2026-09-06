# # 1. Write a python program to add two numbers.
a=int(input("enter the first no : "))
b=int(input("enter the second no : "))
c=a+b
print(c)

# # 2. Write a python program to find remainder when a number is divided by z.
a=int(input("enter the number: "))
c=a%2
print("the reminder will be",c)

# # 3. Check the type of variable assigned using input() function
a=input("enter the number or string : ")
print(type(a))

# 4. Use comparison operator to find out whether ‘aʼ given variable is greater than ‘bʼ or not.
# Take a = 34 and b = 80
a=34 
b=80
print("thee statment a is grater then b is",a>b)

# 5. Write a python program to find an average of two numbers entered by the user.
a=int(input("enter the first number  : "))
b=int(input("enter the second no : "))
print("the Average of these ", (a+b)/2)

# 6. Write a python program to calculate the square of a number entered by the user.
a=int(input("enter the number to square it : "))
print(f"the square of {a} is {a**2}")

# Question 1: Swap Without Temp Variable
a=int(input("enter the first no : "))
b=int(input("enter the second no : "))
print(f"the value of a nd b are {a} and {b}")
a=a+b
b=a-b
a=a-b
print(f"after swaing the value of a and b are {a} and {b}")

# Question 2: Digit Extractor
s=int(input("enter the number :"))
hundred_digit=s//100
a=s%100
tens_digit=a//10
ones_digi=a%10
print(f"The hundred tens and ones value of the three digit no is {hundred_digit},{tens_digit},{ones_digi}")

# Question 3: Time 
a=int(input("enter the secound you want to convert : "))
hour=a//3600
c=a-(hour*3600)
minute=c//60
seconds=c-(minute*60)
print(f"There is mostly {hour} hour ,{minute} minute ,{seconds} seconds left in {a} seconds")

