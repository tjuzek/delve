import json

# Path to the JSON file
input_file = '/home/delve/kaggle/arxiv-metadata-oai-snapshot.json'
# Path to the output text file
output_file = '/home/delve/kaggle/abstracts.txt'

# Open the input JSON file and the output text file
with open(input_file, 'r') as json_file, open(output_file, 'w') as txt_file:
    # Read each line in the JSON file
    for line in json_file:
        # Convert the line from JSON format to a Python dictionary
        data = json.loads(line)
        # Extract the 'abstract' field
        abstract = data['abstract']
        # remove newlines from the abstract
        abstract = abstract.replace("\n", " ")
        # Write the abstract to the text file, followed by a newline
        txt_file.write(abstract.strip() + "\n")  # Adding double newlines for better separation
