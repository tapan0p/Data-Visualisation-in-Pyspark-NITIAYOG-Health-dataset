import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['NITIAYOG']  # Change 'your_database_name' to your actual database name
collection = db['Health']  # Change 'your_collection_name' to your actual collection name

# Path to your CSV file
csv_file_path = 'NDAP.csv'  # Change to the path of your CSV file

# Read CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Convert DataFrame to a list of dictionaries (one dictionary per row)
records = df.to_dict(orient='records')

# Insert data into MongoDB
collection.insert_many(records)

print(f"Data from {csv_file_path} inserted into MongoDB successfully.")
