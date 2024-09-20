
from pymongo.mongo_client import MongoClient
import backend
import os

username = "akhilabhib"
username = os.getenv('u')

passs = 'akhilabhi'
passs = os.getenv('p')
# MongoDB connection URI
uri = f"mongodb+srv://{username}:{passs}@url.lbopx.mongodb.net/?retryWrites=true&w=majority&appName=url"

# Create a new client and connect to the server
client = MongoClient(uri)

# Access the 'akhil' database
db = client['akhil']

# Function to add a URL to the 'url' collection
def add_url(url,point,typ):
    url = url
    typ = typ
    point = int(point)
    count = backend.pointcount(point)
    watch = 0
    collection = db['url']
    data = {'url': url,'typ':typ,'point':point,'count':count,'watch':watch}
    collection.insert_one(data)
    print("URL added successfully!")


