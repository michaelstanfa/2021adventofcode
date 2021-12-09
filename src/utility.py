import os

def load_file_return_as_list(location, file_name):

    with open(f"{location}/{file_name}", "r") as file:
        lines = file.readlines()

        content = []

        for l in lines:
            content.append(l.strip())

    return content