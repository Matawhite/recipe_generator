import csv
import random

file = open("recipe_list.csv", "r")

data = list(csv.reader(file))

selections = random.sample(data, 6)

for item in selections:
    print(item[0])
