from openpyxl import load_workbook
from datetime import datetime
WORKBOOK = load_workbook(filename="C:/Users/joaov/Downloads/Eu.xlsx")

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


def salva_tudo(quantidade, macros, refeicao, data):
    '''
        Salva as calorias, as proteínas e os carboidratos na planilha do Excel.
    '''
    sheet_calorias = WORKBOOK[macros] # Seleciona uma sheet específica(Calorias, Proteina, Carboidratos)

    '''
        Itera por todas as células válidas da sheet e salva o valor passado se o valor original da célula for
        None e se a célula está na coluna que corresponde a data atual.
    '''
    for j in sheet_calorias.columns:
        valida = 0 # Variável para verificar se o valor foi adicionado em alguma célula
        for i in j: # Itera por todas células de uma determinada  coluna


            '''
                Se o valor da célula for igual ao nome da refeição passada, ex: Café, Almoço,...
                
                Então o programa itera pelas seis células adjacentes e verifica se
                o valor de alguma delas é None e se ela está na coluna referente a data de hoje.
                
                Se os dois casos forem verdadeiros o valor passado na variável 'quantidade' é 
                adicionado a célula e a iteração é finalizada.
            '''

            if i.value == refeicao: # Verifica se o nome da refeição passada
                letra = i.coordinate[0] # Recebe a parte literal do endereço da célula.
                numero = i.coordinate[1:] # Recebe a parte númerica do endereço da célula.
                index = 0
                while index < 6: # Itera pela seis células adjacentes
                    letra = chr(ord(letra) + 1) # Pega o valor ASCII da parte literal e soma mais 1
                    n_cel = letra + numero
                    index += 1

                    # Verifica se a célula está vazia e a data
                    if sheet_calorias[n_cel].value is None and valida_data(sheet_calorias, n_cel, data):
                        sheet_calorias[n_cel].value = quantidade
                        valida = 1
                        break
            if valida == 1:
                break
        '''
            Se o valor foi salvo na célula salva a Planilha
        '''
        if valida == 1:
            WORKBOOK.save(filename="C:/Users/joaov/Downloads/Eu.xlsx")
            break


def valida_data(sheet, celula, data):
    '''
        Verifica se a coluna que receberá os dados corresponde ao dia atual.
    '''

    numero = int(sheet[celula].coordinate[1:]) # Recebe a parte númerica do endereço da célula.
    letra = sheet[celula].coordinate[0] # Recebe a parte literal do endereço da célula.
    indice = letra + str(numero)
    dia = data

    '''
        Diminui a parte numérica da célula até chegar a data para fazer verificação.
    '''
    while True:
        k = sheet[indice]
        try:
            k.value.day
        except AttributeError:
            numero-=1
            indice = letra + str(numero)
        else:
            if k.value.day == dia:
                return True
            return False
