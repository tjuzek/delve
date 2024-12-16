import random

file_path = "/home/delve/pubmed_data_years/2020.txt"
sample_size = 10000

with open(file_path, "r") as file:
    lines = file.readlines()
    random_sample = random.sample(lines, sample_size)

with open("/home/delve/input_human_abstracts_sample_2020.txt", "w") as file:
    file.writelines(random_sample)

