
# def copy(file_name, new_file_name):
#     with open(file_name) as file:
#         text = file.read()
#
#     with open(new_file_name, "w") as new_file:
#         new_file.write(text[::-1])
#
# copy("brett.txt", "reversed.txt")

#
# def statistics(file_name):
#     with open(file_name) as file:
#         lines = file.readlines()
#
#     return {
#         "lines": len(lines),
#         "words": sum(len(line.split(" ")) for line in lines),
#         "characters": sum(len(line) for line in lines)}
#
#
# print(statistics("brett.txt"))


def find_and_replace(file_name, find_word, replace_word):
    with open(file_name, mode="w") as file:
        lines = file.read()
        new_lines = lines.replace(find_word, replace_word)
        file.seek(0)
        file.write(new_lines)
        file.truncate()


print(find_and_replace("brett.txt", "Google", "Brett Inc"))

