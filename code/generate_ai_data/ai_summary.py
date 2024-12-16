"""
A module for creating summaries of scientific abstracts using OpenAI's GPT-3 engine.

Usage:
    python ai_summary.py <input_file_path> <output_file_path>
"""

import openai
import re
import os
import logging
import argparse
from dotenv import load_dotenv


# Code has been refactored using Copilot and ChatGPT
# Load environment variables and configure logging
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def read_abstracts(file_path):
    """
    Read abstracts from a file and return a list of abstracts.
    
    Args:
        file_path (str): Path to the file containing abstracts.

    Returns:
        list: A list of abstracts read from the file.
    """
    with open(file_path, "r") as file:
        return file.read().split("\n")

def rewrite_abstracts(abstracts, engine, max_tokens=2000):
    """
    Use OpenAI's API to rewrite a list of abstracts.
    
    Args:
        abstracts (list): List of abstracts to be rewritten.
        engine (str): The GPT model engine to use for rewriting.
        max_tokens (int): Maximum number of tokens to use for each completion.

    Returns:
        list: A list of rewritten abstracts.
    """
    rewritten = []
    for count, abstract in enumerate(abstracts):
        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=f"The following is an abstract of an article. Summarize it in a couple of sentences. \"{abstract}\"",
                max_tokens=max_tokens
            )
            rewritten.append(response.choices[0].text.strip().replace("\n", " "))
            if count % 100 == 0:
                logging.info(f"Processed {count} abstracts")
        except Exception as e:
            logging.error(f"Error at abstract number: {count}: {e}")
    return rewritten

def write_summaries(output_path, summaries):
    """
    Write summaries to a file.
    
    Args:
        output_path (str): Path to the file where the summaries will be written.
        summaries (list): List of summaries to write.
    """
    with open(output_path, "w") as file:
        for summary in summaries:
            file.write(summary + "\n")

def clean_abstracts(file_path):
    """
    Clean abstracts by removing specific patterns.
    
    Args:
        file_path (str): Path to the file containing abstracts to be cleaned.

    Returns:
        str: Cleaned abstracts concatenated into a single string.
    """
    with open(file_path, 'r') as input_file:
        lines = input_file.readlines()

    pattern = re.compile(r'.*?[Aa]bstract:')
    output_string = ""
    for line in lines:
        line = line.strip()
        if "bstract:" in line[:80]:
            line = re.sub(pattern, '', line).strip()
        if "Title:" in line[:25] or " title:" in line[:25]:
            line = ""
        output_string += line + "\n"

    output_string = re.sub(r'\n{2,}', '\n', output_string).replace("\"", "")
    return output_string.strip("\n")

def main():
    """
    Main function to execute the script functionalities.
    """
    parser = argparse.ArgumentParser(description="Process abstracts using OpenAI's API and clean them.")
    parser.add_argument('input_file_path', type=str, help="Path to the input file containing abstracts.")
    parser.add_argument('output_file_path', type=str, help="Path to the output file for storing rewritten abstracts.")
    args = parser.parse_args()

    abstracts = read_abstracts(args.input_file_path)
    rewritten_abstracts = rewrite_abstracts(abstracts, "gpt-3.5-turbo-instruct")
    write_summaries(args.output_file_path, rewritten_abstracts)
    cleaned_output = clean_abstracts(args.output_file_path)
    write_summaries(args.output_file_path, [cleaned_output])


if __name__ == "__main__":
    main()
