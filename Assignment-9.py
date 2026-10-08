import csv
import json


def read_csv(filename):
    with open(filename, "r", newline="") as f:
        return list(csv.DictReader(f))


def write_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def convert_csv_to_json(input_file, output_file):
    data = read_csv(input_file)
    write_json(output_file, data)
    return data


if __name__ == "__main__":
    data = convert_csv_to_json("students.csv", "students.json")
    print("Rows converted:", len(data))
    print("CSV successfully converted to JSON!")