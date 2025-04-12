import pandas
output = {
    "Fur Color": [],
    "Count": []
}

data = pandas.read_csv("data_file.csv")

for color in data["Primary Fur Color"].to_list():
    color = str(color).lower()
    if color == 'nan': continue
    elif color == 'cinnamon': color = "red"
    elif color == 'gray': color = "grey"

    if not color in output["Fur Color"]:
        output["Fur Color"].append(color)
        output["Count"].append(0)
    index = output["Fur Color"].index(color)
    output["Count"][index] += 1

print(output)
output_data = pandas.DataFrame(output)
output_data.to_csv("squirrel_count.csv")