import pymongo

# Create the client
client = pymongo.MongoClient('127.0.0.1', 27017)

# Connect to our database
db = client['ProfileDB']

# Fetch our series collection
series_collection = db['profile']


def insert_document(collection, data):
    """ Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_one(data).inserted_id


new_show = {
    "lastname": "Michail",
    "age": 32
}
print(insert_document(series_collection, new_show))

