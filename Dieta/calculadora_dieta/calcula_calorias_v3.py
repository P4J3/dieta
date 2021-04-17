from time import sleep

from calculadora_dieta.grava_macros_v2 import salva_tudo

lista_alimentos = {
		'arroz_cozido':{'id': 1, 'nome': 'Arroz Cozido', 'calorias': 130, 'proteina': 2.5, 'carboidratos':28.18},
		'feijao_cozido':{'id': 2, 'nome': 'Feijão Cozido', 'calorias': 76, 'proteina': 2.5, 'carboidratos':23.22},
		'porco_assado':{'id': 3, 'nome': 'Porco Assado', 'calorias': 247,'proteina':26.98,'carboidratos':0},
		'frango_assado':{'id': 4, 'nome': 'Frango Assado', 'calorias': 195,'proteina':29.55,'carboidratos':0},
		'ovo_frito':{'id': 5, 'nome': 'Ovo Frito', 'calorias': 194,'proteina':13,'carboidratos':0.93},
		'ovo_cru':{'id': 6, 'nome': 'Ovo Cru', 'calorias': 147,'proteina':12.58,'carboidratos':0.77},
		'batata_doce':{'id': 7, 'nome': 'Batata Doce', 'calorias': 86,'proteina':1.57,'carboidratos':20.12},
		'cuscuz':{'id': 8, 'nome': 'Cuzcuz', 'calorias': 112,'proteina':3.79,'carboidratos':23.22},
		'banana':{'id': 9, 'nome': 'Banana', 'calorias': 89,'proteina':1.09,'carboidratos':22.84},
		'queijo_prato':{'id': 10, 'nome': 'Queijo Prato', 'calorias': 353.33, 'proteina': 24, 'carboidratos': 3.33},
		'presunto':{'id': 11, 'nome': 'Presunto', 'calorias': 163,'proteina': 16.6 , 'carboidratos': 3.83},
		'peixe':{'id': 12, 'nome': 'Peixe', 'calorias': 177, 'proteina': 23.8, 'carboidratos': 0.49},
		'pao_integral':{'id': 13, 'nome': 'Pão Integral', 'calorias':154, 'proteina':3.8, 'carboidratos':28},
		'queijo_mussarela':{'id': 14, 'nome': 'Queijo Mussarela', 'calorias': 286.67, 'proteina': 21, 'carboidratos':33.33},
		'bisteca':{'id': 15, 'nome': 'Bisteca Bovina', 'calorias': 291, 'proteina': 30.1, 'carboidratos': 0}
}

REFEICAO = {
	'Café': 1,
	'Almoço': 2,
	'Tarde': 3,
	'Jantar': 4,
	'Pós-Jantar': 5,
	'Pós-Treino': 6
}


def main():
	total_calorias = 0
	total_proteinas = 0
	total_carboidratos = 0
	menu(total_calorias, total_proteinas, total_carboidratos)


def calorias_macros(alimento, quantidade):
	for i in lista_alimentos:
		if lista_alimentos[i]['id'] == alimento:
			nome = lista_alimentos[i]['nome']
			calorias = round(lista_alimentos[i]['calorias'] * quantidade /100, 2)
			proteina = round(lista_alimentos[i]['proteina'] * quantidade /100, 2)
			carboidratos = round(lista_alimentos[i]['carboidratos'] * quantidade /100, 2)
			
			return {'alimento':nome,'calorias':calorias, 'proteinas':proteina, 'carboidratos': carboidratos}
			# return f'Calorias: {calorias}g\nProteína: {proteina}g\nCarboidratos: {carboidratos}g'
			

	return 'O alimento não está no sistema'


'''def verifica_indice(indice):
	if indice.lower() == "sair":
		exit()
	elif indice.isnumeric() == True:
		return True
	else:
		return input("Digite o índice/Sair: ")
'''


def verifica_indice(total_calorias=0, total_proteinas=0, total_carboidratos=0):
	'''
		Pega o índice do usuáio e decide se:
			1º O programa será fechado
			2º O índice será retornado para o usuário
			3º A refeição será fechada
	'''

	indice = input("Digite o índice/Sair: ")

	if indice.lower() == "sair":
		sair(total_calorias,total_proteinas, total_carboidratos)
	elif indice.isnumeric() is True and int(indice) != 0:
		return int(indice)
	elif int(indice) == 0:
		fechar_refeicao(total_calorias, total_proteinas, total_carboidratos)
	resposta = verifica_indice()
	return int(resposta)

'''
def verifica_quantidade(quantidade):
	while quantidade.isnumeric() == False:
		return input("Digite a quantidade: ")
'''


def verifica_quantidade():
	'''
		Pega o quantidade de alimento naquela refeição e retorna a mesma
	'''
	quantidade = input("Digite a quantidade: ")
	if quantidade.isnumeric() is False:
		quantidade = verifica_quantidade()
	return int(quantidade)


def sair(total_calorias, total_proteinas, total_carboidratos):
	'''
		Imprime o total de calorias e macro nutrientes da refeição e logo em seguida fecha o programa
	'''
	print("=====Refeição=====")
	print(f" Calorias: {str(total_calorias).replace('.',',')} \n Proteinas: {str(total_proteinas).replace('.',',')}\n Carboidratos: {str(total_carboidratos).replace('.',',')}")
	exit()


def fechar_refeicao(total_calorias, total_proteinas, total_carboidratos):
	'''
		Imprime o total de calorias e macro nutrientes da refeição e logo em seguinda chama a função menu() para dar início a uma nova refeição
	'''
	print("=====Refeição=====")
	print(f" Calorias: {str(total_calorias).replace('.',',')} \n Proteinas: {str(total_proteinas).replace('.',',')}\n Carboidratos: {str(total_carboidratos).replace('.',',')}")
	salva_refeicao(total_calorias, total_proteinas, total_carboidratos)
	menu()


def salva_refeicao(total_calorias, total_proteinas, total_carboidratos):
	macros = {'Calorias':total_calorias, 'Proteína':total_proteinas, 'Carboidratos':total_carboidratos}
	print("==Selecione o Tipo de Refeição==")
	for chave, valor in REFEICAO.items():
		print(f"{valor} - {chave}")
	refeicao = input("Selecione[1-6]: ")
	try:
		int(refeicao)
	except ValueError:
		salva_refeicao()

	for chave, valor in REFEICAO.items():
		if int(refeicao) == valor:
			refeicao = chave
			break

	print("==Digite a data==[dd/mm/Y]")
	data = input("Data:")
	for chave, valor in macros.items():
		salva_tudo(valor, chave, refeicao, data)


def menu(total_calorias=0, total_proteinas=0, total_carboidratos=0):

	# Mostra um menu com o Elementos do lista_alimentos
	print()
	print("Selecione o alimento:")
	for i in lista_alimentos.values():
		print(f" {i['id']} - {i['nome']}")
	print()

	# Pega o índice do alimento
	indice = verifica_indice(total_calorias, total_proteinas, total_carboidratos)

	# Pega a quantidade do alimento
	quantidade = verifica_quantidade()

	'''
		Pega os valores nutricionais do alimento e seu nome
	'''
	alimento = calorias_macros(indice,quantidade)
	calorias = alimento['calorias']
	proteina = alimento['proteinas']
	carboidratos = alimento['carboidratos']

	'''
		Imprime as calorias e os macro nutrientes de determinado alimento
	'''
	print(type(calorias))
	print()
	print(f"==={alimento['alimento']}===")
	print(f" Calorias: {str(calorias).replace('.',',')}\n Carboidratos: {str(carboidratos).replace('.',',')}\n Proteína: {str(proteina).replace('.',',')}")

	'''
		Soma os valores nutricionais aos valores da refeição
	'''
	total_calorias +=calorias
	total_proteinas += proteina
	total_carboidratos += carboidratos

	# Chama a função menu novamente para o próximo alimento dessa refeição
	menu(total_calorias, total_proteinas, total_carboidratos)


if __name__ == '__main__':
	main()



