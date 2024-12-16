# Rapid development script to generate experimental items for the Delve project
# The script has yet to be cleaned up / polished in terms of code quality
import openai
import random


# Set your API key here
openai.api_key = "YOUR_OPENAI_API_KEY"


def sample_lines(file_path, num_lines):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = random.sample(lines, num_lines)
    lines = [line.strip() for line in lines]
    return lines


def ai_rewrite_abstract(abstracts, gpt_engine, gpt_prompt, words, num_words, negative):
    c = 0
    abstracts_rewritten = []
    for abstract in abstracts:
        b = 0
        try:
            print(c)
            # Create the prompt for GPT-3
            abstract = abstract.strip()

            if num_words != 0:
                # sample num_words words from the list of words, without replacement
                target_words = random.sample(words, num_words)
                # convert the list of words to a string
                target_words = '\', \''.join(target_words[:-1]) + '\', and \'' + target_words[-1]
                prompt = f"{gpt_prompt} \'{target_words}\': \"{abstract}\""
            else:
                prompt = f"{gpt_prompt} \"{abstract}\""
            print(prompt)
            
            if negative:
                block_words = words + ['sheds', 'highlights', 'valuable', 'examines', 'managing', 'highlighting', 'implications', 'paper', 'scientific', 'ultimately', 'insights']
                blocked_words = 3
                # Check if any block_words are in gpt3_response
                while blocked_words > 0:
                    b += 1
                    if b > 10:
                        gpt3_response = ("Too many attempts, skipping this abstract")
                        break
                    blocked_words = 0
                    # Request GPT-3 completion
                    response = openai.Completion.create(
                        engine = gpt_engine, #engine="gpt-3.5-turbo-instruct""text-davinci-003",  # Replace with the specific GPT-3 engine you prefer
                        prompt = prompt,
                        max_tokens = 2000  # Adjust the token count based on the length of responses you want
                    )
                    # Extract the generated response text
                    gpt3_response = response.choices[0].text.strip()
                    for word in block_words:
                        if word in gpt3_response:
                            blocked_words += 1
                    print(c, blocked_words, b)               
            else:
                focal_words = 0
                while focal_words < 3:
                    b += 1
                    if b > 10:
                        gpt3_response = ("Too many attempts, skipping this abstract")
                        break
                    response = openai.Completion.create(
                        engine = gpt_engine, #engine="gpt-3.5-turbo-instruct""text-davinci-003",  # Replace with the specific GPT-3 engine you prefer
                        prompt = prompt,
                        max_tokens = 2000  # Adjust the token count based on the length of responses you want
                    )
                    # Extract the generated response text
                    gpt3_response = response.choices[0].text.strip()
                    focal_words = 0
                    for word in words:
                        if word in gpt3_response:
                            focal_words += 1
                    print(c, focal_words, b)
                

            gpt3_response = gpt3_response.replace("\n", " ")
            abstracts_rewritten.append(gpt3_response + "\n")
            c += 1
        
        except Exception as e:
            print("Error at abstract number: ", c)
            print(e)
            c += 1
            continue
    
    return abstracts_rewritten


# Set the GPT engine you want to use
gpt_engine = "gpt-3.5-turbo-instruct"  # Replace with the specific GPT-3 engine you prefer
sample_size = 200
words = ['delve', 'showcasing', 'underscores', 'surpassing', 'underscore', 'showcases', 'advancements', 'delves', 'realm', 'delving', 'intricate', 'intricacies', 'surpasses', 'emphasizing', 'boasts', 'comprehending', 'aligns', 'delved', 'groundbreaking', 'underscoring', 'garnered']
more_words = words + ['look into', 'illustrating', 'underlines', 'exceeding', 'underline', 'illustrates', 'improvements', 'looks into', 'area', 'looking into', 'complex', 'complexities', 'exceedes', 'underlining', 'exhibits', 'broad', 'agrees with', 'looked into', 'disruptive', 'underlining', 'attracted attention']

positive_prompt = "Please write a 100-word abstract for the following scientific paper, using words such as"
negative_prompt = "Please write a 100-word abstract for the following scientific paper, making sure not to use words such as"


ai_summaries_file = '/home/delve/create_experimental_items/output_ai_summary_gpt-3.5-turbo-instruct.txt'
ai_summaries = sample_lines(ai_summaries_file, sample_size)

ai_summaries_rewritten_positive = ai_rewrite_abstract(ai_summaries, gpt_engine, positive_prompt, words, 4, False)
ai_summaries_rewritten_negative = ai_rewrite_abstract(ai_summaries, gpt_engine, negative_prompt, more_words, len(more_words), True)

output_file = open('/home/delve/create_experimental_items/TEMPrewrite_ai_summaries.tsv', 'w')
output_file.write("U-S-E-TARGET-WORDS\tAVOID-TARGET-WORDS\n")

for i in range(len(ai_summaries)):
    output_file.write(ai_summaries_rewritten_positive[i].strip() + "\t" + ai_summaries_rewritten_negative[i].strip() + "\t" + str(len(ai_summaries_rewritten_positive[i].split(" "))) + "\t" + str(len(ai_summaries_rewritten_negative[i].split(" "))) + "\n")
output_file.close()
