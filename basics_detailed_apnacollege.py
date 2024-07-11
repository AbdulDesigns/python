"""
name = "abdul"
print(type(name))

a = 2
b = 3
c = "@"
print(a * b * c)

#integer division

number1 = 1.5
number2 = 4
print(number1, (number2 // number1))

#input
value = input("enter the value")
print(value)

#boolean values are case-sensitive
#checking type
aa = 10
bb = 12
print(type(a + b))

#numerical multiplication with string
ab = 2
ac = "hello"
print(ab * ac)

#result of two integer division is float
#you can use integer division to avoid conversion //
num1 = 4
num2 = 2
print(num1 // num2)


checking multiline comments
you can write in multiple lines like this


#conditionals
age = int(input("enter your age:"))
if age > 18:
    print("you are eligible")
elif age == 18:
    print("you are eligible")
else:
    print("you are not eligible")

#single line conditionals statements or ternary operator
food = input("enter your favorite food:")
res = "orange" if food == "Orange" else "no"
print(res)

#using statement
print("sweet") if (food == "jalebi" or food == "khoya") else print("no")
"""


# #using ternary operator calculating salary
# salary = float(input("enter your salary:"))
# tax = salary * (0.1, 0.2) [salary >=50000]
# print(tax)

# assignment operators
# cat = 10
# cat **=10
# print(cat)

# logical operators
# a = 10
# b = 20
# print(not(a<b))
#
# aa = int("10")
# b = "bian"
# print(int(b))

#Q1
# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# print(num1 + num2)

#Q2 - find the area of the square
# side = int (input("enter your side:"))
# print("area=", side**2)

#Q3 - comparision and boolean value
# a = int(input("enter your a:"))
# b = int(input("enter your b:"))
# if a > b:
#     print(True)
# else:
#     print(False)

# res = "true" if a>=b else "False"
# print(res)

# res = ("false", "true")[a>=b]
# print(res)

# print(a>=b)

#strings - escape sequence
# print("hello \ti am abdul.")

# position of strings
# name = "abdul razaq"
# print(name[0])

# slicing -> returns sliced part starting to end value
# fullName = "hercules cycle"
# print(fullName[0:3])
#
# # negative indexing
# print(fullName[-3 : -1])
#
# # string functions
# print(fullName.endswith("le"))
# print(fullName.find("le"))
# print(fullName.replace("le", "me"))
# print(fullName.count("h"))
#
# #string capatilize
# changes_string = fullName.capitalize()
# print(changes_string)

# problem to find highest of 3 numbers

# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# num3 = int(input("enter third number:"))
#
# if (num1 > num2 and num3):
#     print("highest number is", num1)
# elif(num2 > num1 and num3):
#     print("highest number is", num2)
# else:
#     print("highest number is", num3)

#odd or even

# number = int(input("enter your number:"))
# if(number % 2 == 0):
#     print(number, "is an even number")
# else:
#     print(number, "is an odd number")

# lists
# student = ["abdul", 89, "razaq"]
# student.append("added")
# print(student)

# marks = [24, 12, 8, 99]
# # marks.sort(reverse=True)
# # marks.insert(1, 5)
# marks.remove(12)
# marks[0] = "added"
# print(marks)

# Tuples

# collection = (1,2,33,12,54)
# collection[0] = "check"

#problems on list - fav subjects

# subject1 = input("enter your first subject:")
# subject2 = input("enter your second subject:")
# subject3 = input("enter your third subject:")
# sid= []
# sid.append(subject1)
# sid.append(subject2)
# sid.append(subject3)
# print(sid)

# check if the list contains palindrome
# num = [1,2,3,2,1]
# numrev = num.copy() #to copy the num
# numrev.reverse()
# if (num == numrev):
#     print("they are palindrome")
# else:
#     print("they are not palindrome")

#to count the number of students get grade A
# tuples
# grades = ("c", "c", "a", "b", "d", "b", "b", "b")
# a_grade = grades.count("a") #returns the values
# print(a_grade)

# #dictionary
# info = {
#     "name" : "abdul",
#     "school" : "vidya mandir",
#     "is_adult" : "True",
#     24 : "child",
#     True : True,
#     (24, 234) : "challenge"
# }
# # adding value to dictionary
# info["age"] = 32
#
# print(info)

# nested dictionary
# student = {
#     "name" : "abdul",
#     "subjects" : {
#         "maths" : 90,
#         "science": 80,
#
#     },
#     "school" : "vidya mandir"
# }

# print(student["subjects"]["maths"])
# print(student.items())

# student["gender"] = "male"

# # udpdate method
# old_dict = {
#     "name" : "razaq",
# }
# new_dict = {
#     "name" : "india",
#     "age" : 24
# }
#
# old_dict.update(new_dict)
# print(old_dict)

# sets
# breakfast = {"milk", "banana", "roti", "nuts"}
# print(type(breakfast))

# # to create an empty set
# empty = set()
# empty.add(1)
# empty.add(2)
# empty.add("hello")
# print(empty.pop())
# print(empty)

# # union and intersection
# names = {"abdul", "razaq", "rahul"}
# names2 = {"abdul", "gandhi", "monerty"}
# new = names.union(names2)
# print(new)

# problems
# --dictionary--
# meanings = {
#     "table" : ("a peice of futniture", "list of facts and figures"),
#     "cat" : "a small animal"
# }
# print(meanings)

# # --set--
# subjects = {"python", "java", "c++","python" ,"javascript","java", "python", "java", "c++", "c"}
# print(len(subjects))

# --dictionary--
# marks = {}
# maths = int(input("enter your marks:"))
# science = int(input("enter your science:"))
# social = int(input("enter your social:"))
# marks.update({"maths": maths, "science": science, "social": social})
# print(marks)

# --set--
# sets = {
#     ("float", 9.0),
#     ("int", 9),
# }
# print(sets)

#loops
#while
# n: int = 0


# while count <= 5:
#     print(count * "*")
#     count += 1

# while count>= 0 :
#     print(count)
#     count -= 1

#problem - multiplication of 3
# while n <10 :
#     n +=1
#     print(n * 3)

#problem - list and square of numbers
# indx = 0
# num = [1,4, 9, 16, 25, 36, 49, 64, 81, 100]
# while indx < len(num):
#     print(num[indx])
#     indx += 1

# #problem - searching
# index = 0
# x = 49
# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
#
# while index < len(num):
#     if num[index] == x :
#         print("the number found at", index)
#     index += 1

#for in loop
# name = "abdulrazaq"
# for i in name:
#     print(i)

#using range function
# for i in range(1,50,2):
#     print(i)

# #problem - sum of n numbers
# n = 0
# for i in range(5):
#    n +=i
# print(n)

# functions
# def sum_numbers(a, b):
#     print(a + b)
#
# sum_numbers(4, 5)

# average of 3 numbers
# def avg_numbers(a, b, c):
#     return (a + b + c) / 3
#
# avg = avg_numbers(2, 4, 8)
# print(avg)

# usd to inr
# def money_conversion(n):
#     print(80 * n)
#
# money = int(input("enter the amount"))
# money_conversion(money)

# factorial on n using recursion
# def recursion_val(n):
#     if n == 0:
#         return 1
#     print(n)
#     return recursion_val(n-1) * n
#
# recursed_val = recursion_val(6)
# print(recursed_val)

# sum of n natural numbers
# def sum_natural(number, su=0):
#     if number == 0:
#         return
#     else:
#         su += number
#     sum_natural(number - 1)
#     return su
#
#
# sum_total = sum_natural(6)
# print(sum_total)

# def cal_sum(numbers):
#     if numbers == 0:
#         return 0
#     return cal_sum(numbers - 1) + numbers
#
# x = cal_sum(5)
# print(x)

# score = [1, 2, 4]
#
#
# def print_list(lis, index):
#     if index == len(lis):
#         return
#     print(lis[index])
#     print_list(lis,index + 1)
#
#
# print_list(score, 0)

#file io
# f = open("demo.txt", "w")
# # data = f.read()
# # print(data)
# # f.close()
#
# f.write("hello sir ji")
# with open("demo.txt")as f:
#    data = f.read()
#    print(data)
# import os
# os.rename("sample.txt", "demo.txt")

#file io practice
# with open("simpleFile.txt", "w") as f:
#     f.write("Hi Everyone \ngoing to second")
#
# f = open("simpleFile.txt", "r")
# data = f.read()
# new_data = data.replace("second","bad")
# x = data.find("second")
# print(x)

# search the line for a specific word
# def check_line():
#     word = "simple"
#     data = True
#     line = 1
#     with open("simpleFile.txt", "r") as f:
#         while data:
#             line_data = f.readline()
#             if word in line_data:
#                 print(line)
#                 return
#             line += 1
#
#
# print(check_line())

# program to find the even numbers in file
# with open("numbers.txt", "r") as f:
#     read_numbers = f.read()
#     # to split numbers in to list using split method
#     split_numbers = read_numbers.split(",")
#     for i in split_numbers:
#
#         if int(i) % 2 == 0:
#             print(i)

# classes and objects

# class Student:
#     name = "abdul"
#
#     # constructor function
#     def __init__(self, fullname, room, age):
#         self.new_name = fullname
#         self.room = room
#         self.age = age
#     # methods
#     def welcome(self):
#         print("welcome")
#
# s1 = Student("chaloo", 24, 27)
# print(s1.new_name, s1.age, s1.room, s1.welcome())

# bank system

# class Account:
#     print("welcome to savera banking services")
#
#     # creating attributes to intake information
#     def __init__(self, acc_number, acc_name):
#         self.acc_number = acc_number
#         self.__acc_name = acc_name
#
# a1 = Account(122234, "rahul")
# print(a1.acc_name, a1.acc_number)

# inheritance example
# class Car:
#     def __init__(self, type):
#         self.type = type
#
#     @staticmethod
#     def start():
#         print("car started")
#
#     @staticmethod
#     def stop():
#         print("car stopped")

# inherited values
# class Toyota(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#
# ca1 = Toyota("abdul", "diesel")
# print(ca1.type)

# class method
# class Student:
#     name = "abdul"
#
#     @classmethod
#     def changeName(cls, name):
#         cls.name = name
#
# s1 = Student()
# s1.changeName("adil")
# print(Student.name)

# property decorator
#
# class Marks:
#     def __init__(self, phy, maths, sci):
#         self.maths = maths
#         self.phy = phy
#         self.sci = sci
#
#     @property
#     def percent(self):
#         return str((self.maths + self.sci + self.phy) / 3) + "%"
#
#
# s1 = Marks(24, 43, 77)
# s1.maths = 89
# s1.phy = 89
# per = s1.percent  #to calculate variable percentage
# print(per)

#cirlce Project
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

a1 = Circle(4)
newArea = a1.area()
print(newArea)

#company and employee details
# class Employee:
#     def __init__(self, role, dept, sal):
#         self.role = role
#         self.salary = sal
#         self.dept = dept
#
#     def showDetails(self):
#         print(self.dept, self.role, self.salary)
#
# class Engineer(Employee):
#     def __init__(self, age, name, role, dept, salary):
#         super().__init__(role, dept, salary)
#         self.name = name
#         self.age = age
#
# e1 = Engineer(24, "abdul", "developer", "software", 70000)

# addition of complex numbers

class ComplexNum:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def printNumber(self):
        print(self.real ,"i +", self.img,"j")

    # def addition(self, num2):
    #     newReal = self.real +num2.real
    #     newImg = self.img +num2.img
    #     return ComplexNum(newReal, newImg)
    # using dunder functions
    def __add__(self, num2):
        newReal = self.real +num2.real
        newImg = self.img +num2.img
        return ComplexNum(newReal, newImg)



num1 = ComplexNum(2,3)
num1.printNumber()

num2 = ComplexNum(6,4)
print(type(num2))
num2.printNumber()

# # passing object inside method, where we can access the values
# num3 = num1.addition(num2)
# print(num3.printNumber())

# adding thro dunder functions
num3 = num1 + num2
print(num3)