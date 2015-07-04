# notes from the videos

# complex queries


# search in the autos collection for any documents that have Toyota as a manufacturer
autos = db.autos.find({"manufacturer": "Toyota"})

# how to only get certain fields you want back: (only the name field)
# you can use query's and projections together
query = {"manufacturer": "Toyota"}
projection = {"_id": 0, "name": 1}
autos = db.autos.find(query, projection)


# using query operators
query = {"population": {"$gt": 5000, "$lt": 1000}}
cities = db.cities.find(query)


# find documents that only CONTAIN a certain field (1 for true, 0 for false)
db.cities.find({"governmentType" : {"$exists" : 1}}).pretty()


# regex
db.cities.find({"name" : {"$regex": "[Ff]riendship"}},{"_id": 0, "name": 1})




# "in" operator: finds any values that contain any of the values listed(every document containing at least 1 value specified)
db.autos.find({"modelYears" : {"$in" : [1994,1933,1988,1999]}})













