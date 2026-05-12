"""
This script extracts the 'primary_name' of each church from churches.json
and saves them into churches-oneliners.txt, one name per line.
"""
import json
import os

def extract_primary_names():
    json_path = 'ccowa-churches/churches/churches.json'
    output_path = 'ccowa-churches/churches/churches-oneliners.txt'
    
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    primary_names = []
    for entry in data:
        primary_name = entry.get('names', {}).get('primary_name')
        if primary_name:
            primary_names.append(primary_name)

    with open(output_path, 'w', encoding='utf-8') as f:
        for name in sorted(primary_names):
            f.write(f"{name}\n")
    
    print(f"Successfully created {output_path} with {len(primary_names)} names.")

if __name__ == "__main__":
    extract_primary_names()
