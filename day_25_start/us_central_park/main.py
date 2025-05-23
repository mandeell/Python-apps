import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_count = data["Primary Fur Color"].value_counts().reset_index()
color_count.columns = ["Fur Color", "Count"]
# color_count.to_csv("Squirrel_count.csv", index=False)
print(pandas.read_csv("Squirrel_count.csv"))
