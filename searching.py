import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
        if field in data:
            return data[field]

def linear_search(sequence, number):
    pozice = []
    for index in range(len(sequence)):
        if sequence[index] == number:
            pozice.append(str(index))
    pocet = len(pozice)
    output = dict()
    output["positions"] = pozice
    output["count"] = pocet
    return output


def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    print(unordered_numbers)

    print(linear_search(unordered_numbers, 0))



if __name__ == '__main__':
    main()