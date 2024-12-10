"""As given in the first statement of the problem statement I am generating the text file with exact constraints
given in the spec file"""

"""To be on a safer side I am just adding one check for checking the total length of each line in the text file 
to make sure we have received the right data set"""

"""In addition to this we can have multiple checks to make sure we have received the right data and they match exactly
to the offset width that has been given in the spec file, that is if the input file is delimited in some way.(not implemented)"""


import json
import csv

def parse_spec_file(spec_path):
    #Parse the spec.json file to get configuration details.
    with open(spec_path, 'r', encoding='utf-8') as file:
        spec = json.load(file)
    column_names = spec["ColumnNames"]
    offsets = list(map(int, spec["Offsets"]))  # Convert offsets to integers
    fixed_width_encoding = spec["FixedWidthEncoding"]
    include_header = spec["IncludeHeader"].lower()
    delimited_encoding = spec["DelimitedEncoding"]
    return column_names, offsets, fixed_width_encoding, include_header, delimited_encoding

def parse_fixed_width_file(input_file, column_names, offsets, encoding):
    #Parse a fixed-width file into a list of lists.
    data = []
    incorrect_data = []
    field_indices = [0] + [sum(offsets[:i+1]) for i in range(len(offsets))]  # Cumulative offsets

    with open(input_file, 'r', encoding=encoding) as file:
        for line in file:
            if len(line) == sum(offsets):
                fields = [line[field_indices[i]:field_indices[i+1]].strip() for i in range(len(offsets))]
                data.append(fields)
            else:
                # I have just stored the incorrect data here which can later on be sent back to the client in any format for correction.
                # I am not implementing the logic for the same as it is out of the current problem statement requirements.
                incorrect_data.append(line)
    return data,incorrect_data

def write_to_csv(output_file, data, column_names, include_header, encoding):
    #Write parsed data to a CSV file.
    with open(output_file, 'w', newline='', encoding=encoding) as file:
        writer = csv.writer(file)
        if include_header:
            writer.writerow(column_names)
        writer.writerows(data)

if __name__ == "__main__":
    # File paths
    spec_file = "spec.json"
    input_file = "input.txt"
    output_file = "output.csv"

    # Parse the spec.json file
    column_names, offsets, fixed_width_encoding, include_header, delimited_encoding = parse_spec_file(spec_file)

    # Parse the fixed-width file
    parsed_data, parsed_incorrect_data = parse_fixed_width_file(input_file, column_names, offsets, fixed_width_encoding)

    # Write the data to a CSV file
    write_to_csv(output_file, parsed_data, column_names, include_header, delimited_encoding)

    print(f"Parsing completed. Output saved to {output_file}.")
