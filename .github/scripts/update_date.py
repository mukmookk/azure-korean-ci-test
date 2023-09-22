import os
import subprocess
from datetime import date

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
    modified_files = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD~1', 'HEAD']).decode('utf-8').splitlines()
    for file in modified_files:
        if file.endswith('.md') and file.startswith('docs/'):
            update_md_file(file)