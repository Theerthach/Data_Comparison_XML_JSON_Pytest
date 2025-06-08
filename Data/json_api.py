import json

def read_json_from_local(file_path):
    """
    Reads a JSON file from local storage and returns the parsed data.
    
    :param file_path: Path to the JSON file
    :return: Parsed JSON data as a dictionary
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)  # Load and return JSON
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None