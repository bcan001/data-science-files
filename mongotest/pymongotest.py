# http://api.mongodb.org/python/current/tutorial.html

import pymongo

# run this in the console to start mongodb on port 27017
# mongod --dbpath /Users/bencaneba/desktop/nodejs/expressmongo/node_modules/express/data

# create a MongoClient to the running mongod instance and connect to the port that mongo is running in
from pymongo import MongoClient
client = MongoClient('localhost', 27017)


db = client.test_database
# collection = db.test_collection

# print db.collections


import datetime
post = {"author": "Mike","text": "My first blog post!","tags": ["mongodb", "python", "pymongo"],"date": datetime.datetime.utcnow()}

# create posts collection
posts = db.posts
# create a new post with a unique _id
# The value of "_id" must be unique across the collection. insert_one() returns an instance of InsertOneResult. For more information on "_id"
post_id = posts.insert_one(post).inserted_id

# find a post in a collection by query parameters
print posts.find_one({"author": "Mike"})
# find a post in a collection by its unique id
print posts.find_one({"_id": post_id})
print




# insert many documents into a collection at once
new_posts = [{"author": "Mike","text": "Another post!","tags": ["bulk", "insert"],"date": datetime.datetime(2009, 11, 12, 11, 14)},{"author": "Eliot","title": "MongoDB is fun","text": "and pretty easy too!","date": datetime.datetime(2009, 11, 10, 10, 45)}]
result = posts.insert_many(new_posts)
print result.inserted_ids

for post in posts.find():
	print post
print

for post in posts.find({"author": "Mike"}):
	print post
print


# range queries
# only print posts with a date less than d
d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
	print post



