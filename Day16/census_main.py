import pandas
import csv

data = pandas.read_csv("./Day16/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black = len(data[data["Primary Fur Color"] =="Black"])
gray = len(data[data["Primary Fur Color"]=="Gray"])
cinnamon = len(data[data["Primary Fur Color"] =="Cinnamon"])
dict_1 = {"Fur color":["Black","Gray","Cinnamon"],
          "Count":[black,gray,cinnamon]}

dict_data = pandas.DataFrame(dict_1)
dict_data.to_csv("./Day16/Fur_count.csv")


