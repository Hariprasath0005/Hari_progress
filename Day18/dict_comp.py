#names = ["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
# import random
# students = {i:random.randint(1,100) for i in names}
# passed = {i:score for (i, score) in students.items() if score >= 60}
# print(passed)
# print(students)
dict1 = {
    "names":["hari","gan","ram","sam"],
    "score":[50,60,70,80]
}
import pandas
frame = pandas.DataFrame(dict1)
print(frame)

for (index, row) in frame.iterrows():
    if row.names == "hari":
        print(row.score)

