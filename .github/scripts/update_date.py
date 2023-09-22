import os
import subprocess
from datetime import date

def get_modified_files():
    output = subprocess.check_output(
        ['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', 'HEAD'],
        text=True
    )
    print(output)
    return output.strip().split('\n')

def update_md_file(file_path):
    today = date.today().strftime("%m/%d/%Y")
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
    
    for i, line in enumerate(content):
        if line.startswith('update:'):
            content[i] = f'update: {today}\n'
            break
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(content)

if __name__ == "__main__":
    modified_files = get_modified_files()
    print(modified_files)
    for file in modified_files:
        if file.endswith('.md') and file.startswith('docs/'):
            update_md_file(file)