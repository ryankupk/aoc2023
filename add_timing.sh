#!/bin/bash

script_directory="./2023"


# Find all .py files in the specified directory and its subdirectories
find "$script_directory" -type f -name '*.py' | while read script; do
    if ! grep -q 'import time' "$script"; then
        # If 'import time' is not already in the file, add it at the beginning 
        echo -e "import time\n$(cat "$script")" > "$script"
    fi

    # Use awk to process the file and insert timing code in a temp file
    awk '
        /part_one\(inp\)/ {
            print "    start_part_one = time.time()"
            print $0
            next
        }
        /part_two\(inp\)/ {
            print "    start_part_two = time.time()"
            print $0
            print "    end_time = time.time()"
            print "    print(f\"Part one took {start_part_two - start_part_one} seconds\")"
            print "    print(f\"Part two took {end_time - start_part_two} seconds\")"
            next
        }
        { print }
    ' "$script" > "temp_file"

    # Move the temporary file to replace the original script
    mv "temp_file" "$script"
done