"""
 Challenge: JSON-to-Excel Converter Tool

Create a Python utility that reads structured data (like you'd get from an API) from a `.json` file and converts it to a CSV file that can be opened in Excel.

Your program should:
1. Read from a file named `api_data.json` in the same folder.
2. Convert the JSON content (a list of dictionaries) into `converted_data.csv`.
3. Automatically extract field names as CSV headers.
4. Handle nested structures by flattening or skipping them.

Bonus:
- Provide feedback on how many records were converted
- Allow user to define which fields to extract
- Handle missing fields gracefully
"""

import json
import csv
import os

input_file = "api_data.json"
output_file = "converted_data.csv"

def load_json_data(filename):
    if not os.path.exists(filename):
        print("JSON file not found")
        return []
    
    with open(filename, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            print("Invalid JSON format")
            return []

def convert_to_csv(data, output_file):
    if not data:
        print("No data to convert")
        return
    
    if not isinstance(data, list):
        print("JSON must be a list of dictionaries")
        return
    
    # Collect all possible keys
    fieldnames = set()
    for record in data:
        fieldnames.update(record.keys())
    fieldnames = list(fieldnames)

    with open(output_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for record in data:
            clean_record = {}
            for key in fieldnames:
                value = record.get(key, "")
                
                if isinstance(value, (dict, list)):
                    clean_record[key] = ""
                else:
                    clean_record[key] = value
            
            writer.writerow(clean_record)

    print(f"Converted {len(data)} records to {output_file}")

def main():
    print("Converting JSON to CSV...")
    data = load_json_data(input_file)
    convert_to_csv(data, output_file)

if __name__ == "__main__":
    main()