
class Athlete:
	def __init__(self, a_name, a_doc=None, a_times=[]):
		self.name = a_name
		self.doc = a_doc
		self.times = a_times

	def top3(self):
		return str(sorted(set([sanitize(each_item) for each_item in self.times]))[0:3])
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
		return (Athlete(templ.pop(0), templ.pop(0), templ))

	except IOError as err:
		print("Ocorreu um erro: " + err)
		return None

james_data = get_coach_data('james2.txt')
julie_data = get_coach_data('julie2.txt')
mikey_data = get_coach_data('mikey2.txt')
sarah_data = get_coach_data('sarah2.txt')

print(james_data.name + "'s fastest times are: " + james_data.top3())  
print(julie_data.name + "'s fastest times are: " + julie_data.top3())  
print(mikey_data.name + "'s fastest times are: " + mikey_data.top3())  
print(sarah_data.name + "'s fastest times are: " + sarah_data.top3())