student_marks = {"samaviya":99, "atharv":95, "sara":76}
print(student_marks)

print(len(student_marks))
print(student_marks.keys())


print(student_marks.values())

print(student_marks.items())

for i in student_marks.keys():
    print(i)

for i in student_marks.values():
    print(i)

for i,j in student_marks.items():
    print(i,j)
    
student_marks["sara"] = 97
print(student_marks)

student_marks["ayesha"] = 33
print(student_marks)

student_marks.pop("ayesha")
print(student_marks)

print(student_marks.get("samaviya"))
