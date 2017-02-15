from models import *
arquivo = None
try:
	with open('perfis.csv','r') as arquivo:
		for linha in arquivo:
				print linha