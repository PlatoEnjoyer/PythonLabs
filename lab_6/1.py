import json
import csv
import os
import sys
from typing import List, Dict, Any

def json_to_csv(json_file_path: str) -> None:
    if not os.path.exists(json_file_path):
        print(f"Error: File '{json_file_path}' not found.")
        return
    
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{json_file_path}': {e}")
        return
    
    if isinstance(data, dict):
        records = [data]
    elif isinstance(data, list):
        records = data
    else:
        print(f"Error: Unsupported JSON structure in '{json_file_path}'")
        return
    
    if not records:
        print("Error: No records found in JSON file.")
        return
    
    base_name = os.path.splitext(os.path.basename(json_file_path))[0]
    output_path = os.path.join(os.path.dirname(json_file_path), f"{base_name}.csv")

    fieldnames = set()
    for record in records:
        fieldnames.update(record.keys())
    
    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=sorted(fieldnames))
            writer.writeheader()
            writer.writerows(records)
        
        print(f"Successfully converted '{json_file_path}' to '{output_path}'")
        print(f"Created CSV with {len(records)} records and {len(fieldnames)} columns")
    except IOError as e:
        print(f"Error writing to CSV file: {e}")

if len(sys.argv) != 2:
    print("Usage: json2csv.py <json_file>")
    sys.exit(1)
    
json_file_path = sys.argv[1]
json_to_csv(json_file_path)