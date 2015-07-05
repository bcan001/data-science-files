# file to read the parsed data from mongolab


from pymongo import MongoClient  # pymongo>=3.0

mongolab_uri = "mongodb://bcaneba:TheAnswer1@ds047762.mongolab.com:47762/testdb"

client = MongoClient(mongolab_uri,
                     connectTimeoutMS=30000,
                     socketTimeoutMS=None,
                     socketKeepAlive=True)

db = client.get_default_database()
print db.collection_names()

shrooms = db.mushrooms

count_poisonous = 0.00
count_edible = 0.00
count_total = 0.00

for s in shrooms.find():
	count_total += 1
	if s['class'] == "p":
		count_poisonous += 1
	elif s['class'] == "e":
		count_edible += 1

print count_poisonous
print count_edible
print count_total


# entropy parent calculation
import math

# math.log( x )
# entropy = - p1*log(p1) - p2*log(p2)...


# entropy of parent
print ((count_poisonous / count_total)*(math.log(count_poisonous / count_total,2)) + (count_edible / count_total)*(math.log(count_edible / count_total,2)))*-1











