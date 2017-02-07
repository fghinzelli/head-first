# -*- coding:UTF-8 -*-

def cadastrar(nomes):
	print 'Digite o nome:'
	nome = raw_input()
	nomes.append(nome)

def alterar(nomes):
	print 'Qual nome deseja alterar?'
	nome = raw_input()

	if (nome in nomes):
		indice = nomes.index(nome)
		print 'Informe o novo nome:'
		nome_alterado = raw_input()
		nomes[indice] = nome_alterado

def remover(nomes):
	print 'Informe o nome a remover'
	nome = raw_input()
	nomes.remove(nome)


def listar(nomes):
	print 'Exibindo nomes:'
	for nome in nomes:
		print nome

def procurar(nomes):
	print 'Informe o nome a procurar:'
	name_to_find = raw_input()
	if (name_to_find in nomes):
		print 'O nome existe na lista'
	else:
		print 'Nome nao encontrado na lista'

def menu():
	nomes = []
	escolha = ''

	while (escolha != '0'):
		print 'Digite: 1 para cadastrar, 2 para alterar, 3 para remover, 4 para listar, 5 procurar, 6 para regex, 0 para terminar'
		escolha = raw_input()

		if (escolha == '1'):
			cadastrar(nomes)
		elif (escolha == '2'):
			alterar(nomes)
		elif (escolha == '3'):
			remover(nomes)
		elif (escolha == '4'):
			listar(nomes)
		elif (escolha == '5'):
			procurar(nomes)
		elif (escolha == '6'):
			procurar_regex(nomes)

def procurar_regex(nomes):

	import re
	print('Digite a expressão regular:')
	regex = raw_input()
	nomes_concatenados = ''.join(nomes)
	resultados = re.findall(regex, nomes_concatenados)
	print 'Resultado da pesquisa: %s' % (resultados)

menu()


