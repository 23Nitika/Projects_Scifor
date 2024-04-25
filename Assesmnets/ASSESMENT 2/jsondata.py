import json
with open("data.json", "r") as file:
    data = json.load(file)

print("JSON Data:")
print(data)
print()

#Accessing Elements
print("Accessing elements:")
print("First students's name:", data["students"][0]["name"])
print("Second students's age:", data["students"][1]["age"])
print()

print("Modifying data:")
data["students"][0]["age"] = 21
data["students"][1]["grade"] = "A"
print("Modified JSON Data:")
print()

print("Adding new data:")
new_student = {"name": "Dolga", "age": 18, "grade": "B"}
data["students"].append(new_student)
print("Updated JSON Data:")
print(data)
print()

print("Iterating through data:")
print("Student details:")
for student in data["students"]:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Grade:", student["grade"])
    print()

with open("data_updates.json", "w") as file:
    json.dump(data, file)

print("Updated data has been written to 'data_updated.json' file.")

