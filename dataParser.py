import json
import pandas as pd

# Step 1: Read the CSV file
csv_file_path = 'data.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file_path)



# Step 2: Convert DataFrame to JSON string
json_str = df.to_json(orient='records')

# Step 3: Save the JSON string to a file
json_file_path = 'data.json'  # Replace with your desired JSON file path
with open(json_file_path, 'w') as json_file:
    json_file.write(json_str)