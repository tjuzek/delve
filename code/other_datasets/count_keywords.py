"""
This script reads an input text file, counts the frequency of specified target words,
calculates their frequency per million words, and writes the results to an output TSV file.
"""

import string

def main():
    """
    Main function to process the input file and write word frequencies to the output file.
    """
    target_words = [
        'of', 'and', 'the', 'data', 'results', 'i', 'year', 'patients',
        'advancements', 'aligns', 'boasts', 'comprehending', 'delve', 'delves',
        'delved', 'delving', 'emphasizing', 'garnered', 'groundbreaking',
        'intricate', 'intricacies', 'realm', 'showcases', 'showcasing',
        'surpasses', 'surpassing', 'underscore', 'underscores', 'underscoring'
    ]
    word_counts = {word: 0 for word in target_words}
    other_words_count = {}

    input_file_path = "/home/delve/data/output_ai_abstract_from_ai_summary_gpt-4o-mini-assistant.txt"
    output_file_path = "/home/delve/results_and_visualisation/gpt4-mini-assistant_freqs.tsv"

    # Open input and output files using context managers
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        output_file.write("Word\tFrequency\n")

        for line in input_file:
            # Preprocess the line
            line = line.strip().lower()
            line = line.translate(str.maketrans('', '', string.punctuation))
            words = line.split()

            # Count occurrences of each word
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    other_words_count[word] = other_words_count.get(word, 0) + 1

        total_words = sum(word_counts.values()) + sum(other_words_count.values())

        # Calculate frequency per million words and write to output file
        for target_word in target_words:
            frequency_per_million = word_counts[target_word] / total_words * 1e6
            output_file.write(f"{target_word}\t{frequency_per_million:.3f}\n")

if __name__ == "__main__":
    main()
