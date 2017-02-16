from nester import print_lol
import pickle

man = []
other = []
try:
	data = open('sketch.txt')

	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			line_spoken = line_spoken.strip()
			if(role == 'Man'):
				man.append(line_spoken)
			elif(role == 'Other Man'):
				other.append(line_spoken)
		except ValueError:
			pass

except IOError as err:
	print('File Error: ' + str(err))
finally:
	if 'data' in locals():
		data.close()

try:
	# O bloco with se encarrega de fechar o arquivo ao final
	with open("man.txt", "wb") as out_man, open('other.txt', 'wb') as out_other:
		pickle.dump(man, out_man)
		pickle.dump(other, out_other)

except pickle.PickleError as perr:
	print('Pickling Error: ' + str(perr))