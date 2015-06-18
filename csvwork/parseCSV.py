import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
	data = []
	with open(datafile, "rb") as f:
		header = f.readline().split(",")
		counter = 0
		for line in f:
			if counter == 10:
				break
			fields = line.split(",")
			entry = {}
			for i, value in enumerate(fields):
				# strip() method takes off the garbage whitespace around strings
				entry[header[i].strip()] = value.strip()

			data.append(entry)
			counter += 1

	print data
	return data


# test the function
def test():
	datafile = os.path.join(DATADIR,DATAFILE)
	d = parse_file(datafile)
	firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
	tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

	assert d[0] == firstline
	assert d[9] == tenthline

test()