import os
from datetime import datetime

def read_and_modify_file(input_file, output_file):
    try:
        # If the file doesn't exist, create it with some sample content
        if not os.path.exists(input_file):
            with open(input_file, "w") as f:
                f.write("Hello world\nThis is a sample file.\nPython is fun!\n")
            print(f"ℹ️ '{input_file}' did not exist, so it was created with sample content.")

        # Open the input file and read content
        with open(input_file, "r") as f:
            content = f.readlines()

        # Modify: convert all text to uppercase
        modified_content = [line.upper() for line in content]


        #Timestamp the modification
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        modified_content.append(f"\n# Modified on {timestamp}\n")


        # Write modified content to a new file
        with open(output_file, "w") as f:
            f.writelines(modified_content)

        print(f"✅ Modified content has been written to '{output_file}'.")

    except PermissionError:
        print(f"❌ Error: You don’t have permission to read '{input_file}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# ---- MAIN PROGRAM ----
if __name__ == "__main__":
    # Ask user for filename
    filename = input("Enter the name of the file to read: ").strip()
    output_filename = "modified_" + filename

    read_and_modify_file(filename, output_filename)