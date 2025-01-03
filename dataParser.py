import csv
import json


def csv_to_json(csv_file_path, json_file_path):
    # Open the CSV file
    with open(csv_file_path, mode="r", newline="") as csv_file:
        # Read the first row to determine the number of columns
        first_row = csv_file.readline().strip().split(",")
        num_columns = len(first_row)

        # Define headers manually (e.g., "Column1", "Column2", ...)
        headers = ["Date", "Email", "Grade", "GPA", "Pass1", "Pass2", "Pass3"]

        # Reset the file pointer to the beginning of the file
        csv_file.seek(0)

        # Read the CSV file with the defined headers
        csv_reader = csv.DictReader(csv_file, fieldnames=headers)

        # Convert the CSV data to a list of dictionaries
        data = [row for row in csv_reader]

    # Remove the first dictionary (header row)
    data.pop(0)

    for datum in data:
        # Delete date and email
        datum.pop("Date")
        datum.pop("Email")
        # Create a sub-dictionary for passwords
        pass1 = {"Password": datum.pop("Pass1")}
        pass2 = {"Password": datum.pop("Pass2")}
        pass3 = {"Password": datum.pop("Pass3")}

        datum["Passwords"] = {
            "Pass1": pass1,
            "Pass2": pass2,
            "Pass3": pass3,
        }

        for key in datum["Passwords"]:
            datum["Passwords"][key]["Cracked"] = False
            datum["Passwords"][key]["Guesses"] = 0
            datum["Passwords"][key]["Entropy"] = 0

    # Convert the list of dictionaries to a JSON string
    json_data = json.dumps(data, indent=4)

    # Write the JSON string to a file
    with open(json_file_path, mode="w") as json_file:
        json_file.write(json_data)


# Example usage
csv_to_json("data/initial.csv", "data/output.json")
