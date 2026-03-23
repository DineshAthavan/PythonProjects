import pandas

weather_data = pandas.read_csv("weather_data.csv")
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231031.csv")

squirrel_count_list = squirrel_data.value_counts("Primary Fur Color").tolist()
squirrel_color_list = squirrel_data["Primary Fur Color"].dropna().unique().tolist()

squirrel_count_data = pandas.DataFrame(data={"FurColor": squirrel_color_list, "Count": squirrel_count_list})
print(squirrel_count_data)
squirrel_count_data.to_csv("squirrel_count.csv")
