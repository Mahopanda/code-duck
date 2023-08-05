import os
import glob
import ast
import openai
import argparse
from tqdm import tqdm
from .visitor import FunctionAndClassVisitor

def analyze_python_file(file_path, model):
    with open(file_path, 'r') as file:
        code = file.read()

    tree = ast.parse(code)

    visitor = FunctionAndClassVisitor()
    visitor.visit(tree)

    # Create an output file path by appending '_analysis' to the original file name
    output_file_path = f"{os.path.splitext(file_path)[0]}_analysis.txt"

    for function_code in visitor.functions:
        # Create a prompt based on the function code
        message = f'我有以下的 Python 函數:\n{function_code}\n' \
                 '1. 這個函數是否符合 SOLID 原則？\n' \
                 '2. 這個函數是否符合 Pythonic 風格？\n' \
                 '3. 對於這個函數您有什麼改進的建議？\n' \
                 '4. 請撰寫修改後的範例？'

        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "你是一個專業的程式碼審核員。"},
                {"role": "user", "content": message},
            ],
        )

        with open(output_file_path, 'a') as f:
            f.write(f"For function:\n{function_code}\n\n")
            f.write(f"Response:\n{response['choices'][0]['message']['content'].strip()}\n\n")

    for class_code in visitor.classes:
        # Create a prompt based on the class code
        message = f'我有以下的 Python 類:\n{class_code}\n' \
                 '1. 這個類是否符合 SOLID 原則？\n' \
                 '2. 這個類是否符合 Pythonic 風格？\n' \
                 '3. 對於這個類您有什麼改進的建議？\n' \
                 '4. 請撰寫修改後的範例'

        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "你是一個專業的程式碼審核員。"},
                {"role": "user", "content": message},
            ],
        )

        with open(output_file_path, 'a') as f:
            f.write(f"For class:\n{class_code}\n\n")
            f.write(f"Response:\n{response['choices'][0]['message']['content'].strip()}\n\n")

def analyze_python_directory(dir_path, model, show_progress=False):
    if not os.path.isdir(dir_path):
        raise ValueError(f"Invalid directory: {dir_path}")

    python_files = glob.glob(f"{dir_path}/**/*.py", recursive=True)

    if show_progress:
        python_files = tqdm(python_files, desc='Analyzing')

    for file_path in python_files:
        print(f"Checking: {file_path}")
        analyze_python_file(file_path, model)

def main():
    parser = argparse.ArgumentParser(description='Analyze Python code.')
    parser.add_argument('-d', '--directory', required=True, help='Directory to analyze.')
    parser.add_argument('-k', '--key', required=True, help='OpenAI API Key.')
    parser.add_argument('-m', '--model', default="gpt-3.5-turbo-16k-0613", help='OpenAI Model to use.')
    parser.add_argument('-p', '--progress', action='store_true', help='Show progress.')
    
    args = parser.parse_args()

    if not args.key:
        raise ValueError("Invalid OpenAI API key.")

    openai.api_key = args.key
    analyze_python_directory(args.directory, args.model, show_progress=args.progress)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
