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


def calc_prob(instances,total):
	return instances / total

def calc_entropy():
	pass


# entropy of parent
parent_entropy = ((count_poisonous / count_total)*(math.log(count_poisonous / count_total,2)) + (count_edible / count_total)*(math.log(count_edible / count_total,2)))*-1


# calc entropy for best attribute ODOR
e(a) = -[p(poisonous) * log(p(poisonous)) + p(edible) * log(p(edible))] # for all mushrooms that have odor 'a'
e(c) = -[p(poisonous) * log(p(poisonous)) + p(edible) * log(p(edible))] # for all mushrooms that have odor 'c'
e(f) = -[p(poisonous) * log(p(poisonous)) + p(edible) * log(p(edible))] # for all mushrooms that have odor 'f'
e(m) = -[p(poisonous) * log(p(poisonous)) + p(edible) * log(p(edible))] # for all mushrooms that have odor 'm'
e(l) = -[p(poisonous) * log(p(poisonous)) + p(edible) * log(p(edible))] # for all mushrooms that have odor 'l'
e(p) = -[p(poisonous) * log(p(poisonous)) + p(edible) * log(p(edible))] # for all mushrooms that have odor 'p'
e(n) = -[p(poisonous) * log(p(poisonous)) + p(edible) * log(p(edible))] # for all mushrooms that have odor 'n'

# information gain for ODOR
IG(ODOR) = parent_entropy - [p(a)*e(a) + p(c)*e(c) + ...]  






