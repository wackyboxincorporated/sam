import os
import sys

def generate_prefixed_file_list(output_filename="file_list.txt"):
    prefix = input("Enter the prefix: ")
    script_name = os.path.basename(__file__) if "__file__" in globals() else ""
    current_directory = os.path.abspath(os.getcwd())
    
    entries = []
    
    try:
        items = sorted(os.listdir(current_directory))
    except OSError as err:
        print(f"Error accessing directory: {err}", file=sys.stderr)
        return

    for item in items:
        item_path = os.path.join(current_directory, item)
        
        # Only process regular files, skip the script itself and the output file
        if os.path.isfile(item_path):
            if item == script_name or item == output_filename:
                continue
            entries.append(f"{prefix}{item}")

    try:
        with open(output_filename, "w", encoding="utf-8") as out_file:
            for entry in entries:
                out_file.write(f"{entry}\n")
        print(f"Successfully wrote {len(entries)} items to {output_filename}")
    except OSError as err:
        print(f"Error writing to output file: {err}", file=sys.stderr)

if __name__ == "__main__":
    generate_prefixed_file_list()

