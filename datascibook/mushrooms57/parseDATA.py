from pymongo import MongoClient  # pymongo>=3.0

mongolab_uri = "mongodb://bcaneba:TheAnswer1@ds047762.mongolab.com:47762/testdb"

client = MongoClient(mongolab_uri,
                     connectTimeoutMS=30000,
                     socketTimeoutMS=None,
                     socketKeepAlive=True)

db = client.get_default_database()
print db.collection_names()

shrooms = db.mushrooms

# user = {"name": "William Caneba", "email": "wcaneba@gmail.com"}
# users = db.users
# user_id = users.insert_one(user).inserted_id

# for u in users.find():
# 	print u


import os

DATADIR = ""
DATAFILE = "agaricus-lepiota.data.csv"


def parse_file(datafile):
	data = []
	with open(datafile, "rb") as f:
		header = f.readline().split(",") # the first row is a header row
		for line in f:
			fields = line.split(",")
			entry = {}
			for i, value in enumerate(fields):
				# strip() method takes off the garbage whitespace around strings
				entry[header[i].strip()] = value.strip()
			data.append(entry)
	return data


def insert_data():
	datafile = os.path.join(DATADIR,DATAFILE)
	d = parse_file(datafile)

	result = shrooms.insert_many(d)

insert_data()





