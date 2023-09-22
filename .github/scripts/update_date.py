import sys
import logging
import ast
from datetime import date

logging.basicConfig(level=logging.DEBUG)
def update_md_file(file_path):
    today = date.today().strftime("%m/%d/%Y")
    logging.debug(f'Updating {file_path} with {today}')
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
    
    for i, line in enumerate(content):
        if line.startswith('update:'):
            content[i] = f'update: {today}\n'
            break
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(content)
        logging.debug(f'Updated {file_path} with {today}')

def main():
    modified_files_string = sys.argv[1].replace("[", "").replace("]", "").replace("'", "")
    modified_files = modified_files_string.split(",")
    logging.debug(f'Modified files: {modified_files}')

    for file in modified_files:
        if file.endswith('.md'):
            update_md_file(file)

if __name__ == "__main__":
    main()