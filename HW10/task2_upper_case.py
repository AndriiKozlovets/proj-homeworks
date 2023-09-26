# Open task2_first_file.txt
with open("HM10/task2_first_file.txt", "r") as source_file:
    content = source_file.read()

# Upper case
with open("HM10/task2_second_file.txt", "w") as dest_file:
    dest_file.write(content.upper())
