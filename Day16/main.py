import csv

#with open("./Day16/weather_data.csv") as w_data:
#    data = csv.reader(w_data)
#    temp = []
#   for i in data:
#        if i[1] != "temp":
#            temp.append(int(i[1]))
#    print(temp)

import pandas
data = pandas.read_csv("./Day16/weather_data.csv")
#print(data,"\n")

dict = data.to_dict()
#print(dict)

list = data["temp"].to_list()
#print(list)

#add = 0
#for i in list:
#    add +=i
#print(add/len(list))

#print(data["temp"].mean())
#a = 0
#for i in list:
#    if i > a :
#        max = i
#    a = i
#print(max)

max = data['temp'].max()

#print(data[data.temp == max])

monday = data[data.day == "Monday"]
c = monday.temp
f = (c*1.8)+32
#print(f)

dict_1 = {"names":["hari","ganesh","ram","sam"],
          "marks":[1,2,3,4] }
dict_data = pandas.DataFrame(dict_1)
dict_data.to_csv("./Day16/sample.csv")


