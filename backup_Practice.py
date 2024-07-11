name = "tony stark"
#find functionality
print(name.find('s'))
#keywords like in are the part of programming language
print('S' in name)  #returns true/false
#arithmatic operations
print(5 // 2)  #returns values without decimals
#remainder Operator
print(5 % 2)
#power operator
print(5 ** 2)

#shortcuts
i = 6
i *= 3
print(i)

#logical Operators and or
print(2 > 3 > 2)
print(not 2 > 3)

#conditional statements
if i > 22:
    print('i is greater than than 22')
elif i < 22:
    print("i is less than 22")

#mini project calculator
first = input("enter the first number")
operator = input("enter the operator(+,_,*,/)")
second = input("enter the second number")
#conversion of string to int
first = int(first)
second = int(second)
if operator == '+':
    print(first + second)
elif operator == '_':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    print(first / second)
else:
    print("Invalid operator")

#loops
i = 1
while i <= 10:
    print(i * "*")
    i += 1
#for loop
for item in range(5):
    print(item)
for food in ["apple", "banana", "cherry"]:
    print(food)
for i in range(2, 20, 2):
    print(i)
