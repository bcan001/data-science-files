# notes from the videos

# complex queries


# search in the autos collection for any documents that have Toyota as a manufacturer
autos = db.autos.find({"manufacturer": "Toyota"})

# how to only get certain fields you want back: (only the name field)
query = {"manufacturer": "Toyota"}
projection = {"_id": 0, "name": 1}
autos = db.autos.find(query, projection)






