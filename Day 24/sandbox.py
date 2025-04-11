with open("my_file.txt", "w") as file:
    file.write("Some text")

my_file = open("my_file.txt", 'r')
print(my_file.read())
my_file.close()

with open("../my_new_file.txt", 'w') as file:
    file.write("It is my new file")