import re

input_file = open("/home/delve/kaggle/wiki_cleaned_2.txt", "r")
output_file = open("/home/delve/kaggle/wiki_cleaned_3.txt", "w")

for line in input_file:
    line = line.strip()
    #line = re.sub(r'<.*?>', '', line)
    #line = re.sub(r'{{.*?}}', '', line)
    line = re.sub(r'http[s]?://\S+|www\.\S+', '', line)
    #if not line.startswith(('*', '|', '{', '=', '<', '[', '#', '!', '}', ';', 'File:')):
    if len(line) > 0:
        output_file.write(line + "\n")

input_file.close()
output_file.close()