"""
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    # print(contents.rstrip())

print(contents)
"""

file_path = 'pi_digits.txt'
with open(file_path) as file_object:
    for line in file_path:
        print(line)

file_path_name = 'programming.txt'
content = 'Hello there, this is sagor from Dhaka-Bangladesh. I love programming'
with open(file_path_name, 'w') as write_file_object:
    write_file_object.write(content)
    write_file_object.write("\nHello this is added new line content")
