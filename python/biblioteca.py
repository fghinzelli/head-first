def gera_nome_convite(convite):
	posicao_final = len(convite)
	posicao_inicial = posicao_final - 4
	parte1 = convite[0:4]
	parte2 = convite[posicao_inicial: posicao_final]
	return parte1 + ' ' + parte2

def envia_convite(nome):
	return 'Enviando convite para ' + nome

def processa_convite(convite):
	return envia_convite(gera_nome_convite(convite))
