import json

input_file = open("original_data.json")
json_array = json.load(input_file)
car_list = []

for index, item in enumerate(json_array):
    car_dict = {
        "model": "coreapp.car",
        "pk": index,
        "fields": {
            "name": item["Name"],
            "miles_per_gallon": item["Miles_per_Gallon"],
            "cylinders": item["Cylinders"],
            "displacement": item["Displacement"],
            "horsepower": item["Horsepower"],
            "weight_in_lbs": item["Weight_in_lbs"],
            "acceleration": item["Acceleration"],
            "year": item["Year"],
            "origin": item["Origin"],
        },
    }
    car_list.append(car_dict)

with open("./info_service/fixtures/coreapp_seeds.json", "w") as fout:
    json.dump(car_list, fp=fout, indent=4)
