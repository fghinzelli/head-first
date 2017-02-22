
def sanitize(time_string):
	""" 
	Substitui os caracters '-' e ':' por virgula
	"""
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return time_string
	(min, secs) = time_string.split(splitter)
	return (min + '.' + secs)

def read_file(file_name):
	try:
		with open(file_name) as ln:
			data = ln.readline()
		return(data.strip().split(','))
	except IOError as err:
		print("Ocorreu um erro: " + err)
		return None

print(sorted(set([sanitize(each_item) for each_item in read_file("james.txt")]))[0:3])
print(sorted(set([sanitize(each_item) for each_item in read_file("julie.txt")]))[0:3])
print(sorted(set([sanitize(each_item) for each_item in read_file("mikey.txt")]))[0:3])
print(sorted(set([sanitize(each_item) for each_item in read_file("sarah.txt")]))[0:3])

