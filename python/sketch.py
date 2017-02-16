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
	with open("man.txt", "w") as out_man, open('other.txt', 'w') as out_other:
		print(man, file=out_man)
		print(other, file=out_other)

except IOError as err:
	print('File Error: ' + str(err))