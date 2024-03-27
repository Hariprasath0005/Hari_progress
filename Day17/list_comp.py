# a = [1,2,3,4]
# b = [i+1 for i in a]
# print(b)
# a = []
# for i in range(1,5):
#     b = i*2
#     a.append(b)
# print(a)

names = ["Alex","Beth","Caroline","Dave","Elanor","Freddie"]

a = [i.upper() for i in names if len(i)>5 ]
print(a)