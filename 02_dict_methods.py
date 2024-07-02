marks = {
    "Mohit": 100, 
    "Harry": 56,
    "Rohan": 23,
    0: "Harry"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry": 90})
print(marks)
print(marks.get("Mohit")) # 13 and 14 are not same because 13 give none value 
print(marks["Mohit"]) # if key not exist but 14 give error

