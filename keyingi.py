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