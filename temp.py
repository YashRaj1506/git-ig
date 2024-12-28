import os

# Directory containing your files
directory = "/home/yash/PycharmProjects/gitignorer/gitignore"


# for filename in os.listdir(directory):
#
#     if filename[0].isupper():
#         new_filename = filename[0].lower() + filename[1:]
#         old_file = os.path.join(directory, filename)
#         new_file = os.path.join(directory, new_filename)
#         os.rename(old_file, new_file)
#         print(f"Renamed: {filename} -> {new_filename}")

list_of_tech = []


def first_names(directory):
    for filename in os.listdir(directory):
        first_part = filename.split(".")[0].lower()
        list_of_tech.append(first_part)

    for i in range(len(list_of_tech)):
        print(list_of_tech[i])


def pri():
    print(list_of_tech)


if __name__ == "__main__":
    first_names("/home/yash/PycharmProjects/gitignorer/gitignore")
    pri()
