import csv
import random
import string
from datetime import datetime

# Generate random first names and last names
def generate_random_name():
    return ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10)))

# Generate random addresses
def generate_random_address():
    house_number = random.randint(1, 9999)
    street_name = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 12)))
    city = random.choice(["Springfield", "Gotham", "Metropolis", "Rivendell", "Hogsmeade"])
    state = random.choice(["CA", "TX", "NY", "FL", "WA"])
    zip_code = random.randint(10000, 99999)
    return f"{house_number} {street_name} St, {city}, {state}, {zip_code}"

# Anonymize data in a CSV file
def anonymize_csv(input_file, output_file, chunk_size=100000):
    with open(input_file, mode='r', encoding='utf-8') as infile, \
         open(output_file, mode='w', encoding='utf-8', newline='') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        # Write header to the output file
        writer.writeheader()
        
        buffer = []
        for row in reader:
            # Anonymize the specified columns
            row['first_name'] = generate_random_name()
            row['last_name'] = generate_random_name()
            row['address'] = generate_random_address()
            buffer.append(row)
            
            # Write buffer to output file in chunks
            if len(buffer) >= chunk_size:
                writer.writerows(buffer)
                buffer = []

        # Write any remaining rows in the buffer
        if buffer:
            writer.writerows(buffer)

# Generate a sample large CSV file for testing
def generate_large_csv(file_name, num_rows):
    with open(file_name, mode='w', encoding='utf-8', newline='') as file:
        fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        for _ in range(num_rows):
            writer.writerow({
                'first_name': generate_random_name(),
                'last_name': generate_random_name(),
                'address': generate_random_address(),
                'date_of_birth': datetime.strftime(
                    datetime(
                        random.randint(1950, 2010),
                        random.randint(1, 12),
                        random.randint(1, 28)
                    ), "%Y-%m-%d")
            })

# Main execution
if __name__ == "__main__":
    # Generate a test CSV file with 2 million rows (~2GB depending on content length)
    input_csv = "large_dataset.csv"
    output_csv = "anonymized_dataset.csv"

    generate_large_csv(input_csv, 2000000)

    # Anonymize the data
    anonymize_csv(input_csv, output_csv)
