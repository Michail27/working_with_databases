from pymongo import *

# запуск сервера
# "C:\Program Files\MongoDB\Server\4.4\bin\mongod.exe" --dbpath="c:\data\db"
# "C:\Program Files\MongoDB\Server\4.2\bin\mongo.exe"

# Create the client
client = MongoClient('mongodb://localhost:27017')
db = client['test_database']
courses = db.courses

data = {
    "lastname": "Petr",
    "age": 20
}


def insert_one_document(collection, data):
    """ Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_one(data).inserted_id


data1 = [{
    "lastname": "Ivan",
    "age": 25},
    {"lastname": "Petr",
    "age": 39}]


def insert_several_document(collection, data):
    """ Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_many(data).inserted_id


def read_document(collection, elements, multiple=False):
    """ Function to retrieve single or multiple documents from a provided
    Collection using a dictionary containing a document's elements.
    """
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)


def update_document(collection, query_elements, new_values):
    """ Function to update a single document in a collection.
    """
    collection.update_one(query_elements, {'$set': new_values})


def delete_document(collection, query):
    """ Function to delete a single document from a collection.
    """
    collection.delete_one(query)

# Simpl
# db.users.find().limit(3).skip(3)
# db.users.find().sort({name: 1})
#  db.users.find ({name: "Tom"}, {languages: {$slice : [-1, 1]}});
#  db.users.find({name: "Tom"}).count()
# db.users.distinct("name") # Уникальные имена
# db.users.find ({age: {$lt : 30}}) # <30
# db.users.find ({age: {$gt : 30}}) # >30
# db.users.find ({$or : [{name: "Tom"}, {age: 22}]})


if __name__ == "__main__":
    rez = insert_one_document(courses, data)
    print(rez)

    # insert_several_document(courses, data1)

    # print(courses.count_documents({}))  # количество записей

    # id_ = read_document(courses, {'lastname': 'Ilya'})

    # new_show = {
    #     "name": "FRIENDS",
    #     "year": 1995
    # }
    # id_ = insert_one_document(courses, new_show)
    # update_document(courses, {'_id': id_}, {'name': 'F.R.I.E.N.D.S'})
    # result = read_document(courses, {'_id': id_})
    # print(result)

    # delete_document(courses, {'name': 'F.R.I.E.N.D.S'})
    # result = read_document(courses, {'name': 'F.R.I.E.N.D.S'})
    # print(result)





