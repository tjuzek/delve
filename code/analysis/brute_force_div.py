"""
A module for identifying significant changes in word usage between two text corpora.

Usage:
    python brute_force_div.py --file2020 <file_path_2020> --file2024 <file_path_2024> --output <output_path>
"""

import sys
import string
from scipy.stats import chi2_contingency

# Code has been refactored using Copilot and ChatGPT

def count_words(text):
    """
    Count the frequency of each word in the provided text.
    
    Args:
    text (iterable): An iterable of strings (e.g., lines of text).
    
    Returns:
    tuple: A dictionary of word frequencies and the total number of words.
    """
    freq_dct = {}
    total_words = 0
    translator = str.maketrans('', '', string.punctuation)
    
    for line in text:
        line = line.strip().lower().translate(translator)
        words = line.split()
        for word in words:
            freq_dct[word] = freq_dct.get(word, 0) + 1
            total_words += 1
    
    return freq_dct, total_words

def chi_sq_test(word, data2020, data2024, total2020, total2024, min_opm):
    """
    Perform a chi-squared test to determine if the usage of 'word' is significantly different.
    
    Args:
    word (str): The word to test.
    data2020, data2024 (dict): Dictionaries of word frequencies for 2020 and 2024.
    total2020, total2024 (int): Total words in 2020 and 2024.
    min_opm (float): Minimum occurrences per million words for significance testing.
    
    Returns:
    bool: True if the change in word usage is statistically significant.
    """
    if word in data2020:
        observed = [data2020[word], total2020 - data2020[word]]
    else:
        observed = [min_opm, total2020 - min_opm]
    
    expected = [data2024.get(word, 0), total2024 - data2024.get(word, 0)]
    chi2, p_value, _, _ = chi2_contingency([observed, expected])
    
    return p_value < 0.05

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_path2020> <input_path2024> <output_path>")
        sys.exit(1)
    
    input_path2020 = sys.argv[1]
    input_path2024 = sys.argv[2]
    output_path = sys.argv[3]

    with open(input_path2020, 'r', encoding='utf-8') as file:
        freq2020, total2020 = count_words(file)
    
    with open(input_path2024, 'r', encoding='utf-8') as file:
        freq2024, total2024 = count_words(file)
    
    freq_diff = {}
    min_opm_2020 = 1000000 / total2020
    
    for word, freq in freq2024.items():
        old_freq = freq2020.get(word, min_opm_2020)
        freq_diff[word] = ((freq - old_freq) / old_freq) * 100
    
    sorted_diff = sorted(freq_diff.items(), key=lambda x: x[1], reverse=True)
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write("word\tchange (%)\topm 2020\topm 2024\tsignificant\n")
        for word, change in sorted_diff:
            is_significant = chi_sq_test(word, freq2020, freq2024, total2020, total2024, min_opm_2020)
            file.write(f"{word}\t{change:.2f}\t{freq2020.get(word, min_opm_2020):.2f}\t{freq2024.get(word, 0):.2f}\t{is_significant}\n")
