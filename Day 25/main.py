import csv
import pandas

# def average(list):
#     sum = 0
#     for item in list:
#         sum += int(item)
#     return sum/len(list)

# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)
#
# with open("weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

data = pandas.read_csv("weather_data.csv")
# print(data["temp"].to_list())
# print( average(data["temp"].to_list()) )
# print( data["temp"].mean() )
# print( data["temp"].max() )
#
# #print row
# print( data[data.day == "Monday"])
# print( data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# # print(f"Monday temp in C: {int(monday.temp[0])}")
# # print(f"Monday temp in F: {((int(monday.temp[0]))*9/5)+32}")

#Create dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("my_new_csv_file.csv")


