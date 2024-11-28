files = ['pam1.txt', 'pam2.txt', 'pam3.txt']

file_contents = {}

for filename in files:
    with open(filename, 'r', encoding='utf-8') as file:
        contents = file.readlines()
        file_contents[filename] = contents

sorted_files = sorted(file_contents.items(), key=lambda item: len(item[1]))

output_file = 'result.txt'  
with open(output_file, 'w', encoding='utf-8') as outfile:
    for filename, contents in sorted_files:
        outfile.writelines(contents)