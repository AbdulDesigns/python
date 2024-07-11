#lists
marks = [24, 43, 52, 43]
print(marks)

#addition of item to list
marks.append(49)
print(marks)

#insert the element at particular place
marks.insert(0, 909)
print(marks)

#to find the length of list
print(len(marks))

#while loop on list
i = 0
while i < len(marks):
    print(marks[i])
    i += 1

names = ["abdul", "razaq", "manish", "raaz"]
for name in names:
    if name == "manish":
        break
    print(name)

#tuples are immutable set of items
veggies = ("carrot", "peas", "cabbage")

#sets in python
#in sets index wont exist
toys = {"car", "jeep", "cycle"}

#dictionary
#it is similar to the object in js

cars = {
    "cheap": "maruti",
    "mid": "fiat",
    "expensive": "mercedez"
}
print(cars)

cars["luxury"] = "BMW"
print(cars)

cars['cheap'] = "nano"
print(cars)

print(cars['cheap'])

del cars['cheap']
print(cars)

print("BMW" in cars["luxury"])


#functions
def pizza():
    print("your pizza is ordered")


pizza()
