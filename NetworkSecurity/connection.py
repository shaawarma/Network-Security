from pymongo import MongoClient
from urllib.parse import quote_plus

# Replace these with your actual username and password
username = "varunvassagudam_db_user"
password = "varun123"  # put your actual password here
encoded_password = quote_plus(password)

# Replace <cluster-url> with your Atlas cluster host
cluster_url = "cluster0.b359khx.mongodb.net"

# Database name (optional)
database_name = "test_db"

# Connection string
uri = "mongodb+srv://varunvassagudam_db_user:varun123@cluster0.b359khx.mongodb.net/?retryWrites=true&w=majority"
# Create client
client = MongoClient(uri)

# Test connection
try:
    client.admin.command("ping")
    print("Connected to MongoDB Atlas!")
    db = client[database_name]  # access your database
except Exception as e:
    print("Connection failed:", e)
