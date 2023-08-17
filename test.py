import os

output_file = 'output.txt'
source_folder = './addons' 

with open(output_file, 'w') as f:
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as source:
                    content = source.read()

                f.write(f'{file_path}\n```py\n{content}\n```\n')

print('Done exporting Python source folder to', output_file)