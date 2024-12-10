import random
import string
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Anonymize Large CSV") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .getOrCreate()


# Define UDFs for anonymization
def random_name():
    """Generate a random name."""
    return ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10)))

def random_address():
    """Generate a random address."""
    house_number = random.randint(1, 9999)
    street_name = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 12)))
    city = random.choice(["Springfield", "Gotham", "Metropolis", "Rivendell", "Hogsmeade"])
    state = random.choice(["CA", "TX", "NY", "FL", "WA"])
    zip_code = random.randint(10000, 99999)
    return f"{house_number} {street_name} St, {city}, {state}, {zip_code}"

# Register UDFs
random_name_udf = udf(random_name, StringType())
random_address_udf = udf(random_address, StringType())

# Load CSV into a Spark DataFrame
input_csv = "large_dataset.csv"  # Replace with your CSV file path
df = spark.read.csv(input_csv, header=True)

# Display initial data (optional)
print("Original Data:")
df.show(5)

# Apply UDFs to anonymize columns
anonymized_df = df.withColumn("first_name", random_name_udf()) \
                  .withColumn("last_name", random_name_udf()) \
                  .withColumn("address", random_address_udf())

# Display anonymized data (optional)
print("Anonymized Data:")
anonymized_df.show(5)

# Write the anonymized data back to CSV
output_csv = "anonymized_large_dataset.csv"
anonymized_df.write.csv(output_csv, header=True)

# Stop Spark session
spark.stop()
