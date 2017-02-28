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

def get_coach_data(file_name):
	try:
		with open(file_name) as ln:
			data = ln.readline()

		templ = data.strip().split(',')
		return ({'Name': templ.pop(0),
					  'DOB': templ.pop(0),
					  'Times': str(sorted(set([sanitize(each_item) for each_item in templ]))[0:3])})
	except IOError as err:
		print("Ocorreu um erro: " + err)
		return None

james_data = get_coach_data('james2.txt')
julie_data = get_coach_data('julie2.txt')
mikey_data = get_coach_data('mikey2.txt')
sarah_data = get_coach_data('sarah2.txt')

print(james_data['Name'] + "'s fastest times are: " + james_data['Times'])  
print(julie_data['Name'] + "'s fastest times are: " + julie_data['Times'])  
print(mikey_data['Name'] + "'s fastest times are: " + mikey_data['Times'])  
print(sarah_data['Name'] + "'s fastest times are: " + sarah_data['Times'])