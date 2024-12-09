"""
Dictionary
"""
car_0 = {"model" : "Bugatti" , "colour" : "White"}
print(car_0["model"])

student = {"name" : "Jony",
           "last name" : "John",
           "age" : 21,
           "profession" : "Data Analytic"}
print(student)
student["university"] = "Harvard"
print(student)

fruits = {}
fruits[1] = "Apple"
print(fruits)
fruits[2] = "Banana"
print(fruits)
del fruits[2]
print(fruits)

"""
next lesson
"""

info_people = {
    "Joe" : "Iphone X",
    "Xo" : "Redmi",
    "Roy" : "Job"
}
print(info_people.items())
for key, value in info_people.items():
    print(f"Key is: {key}")
    print(f"Value is: {value}\n")

