# with open("weather_data.csv") as data_file:
#     data = data_file.read()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
    # for row in data:
    #     if row[1] != "temp":
    #         temperature.append(int(row[1]))
    # print(temperature)
import pandas

# data = pandas.read_csv("weather_data.csv")
#
# # data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
# # print(temp_list)
# # average_temp = sum(temp_list)/len(temp_list)
# # print(f"The average of temp is: {average_temp}")
# monday = data[data.temp == data.temp.min()]
# monday_temp = monday.temp[0]
# monday_temp_f= (monday_temp * 9/5) + 32
# print(monday_temp_f)

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56,65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")