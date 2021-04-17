from openpyxl import load_workbook
from datetime import datetime
WORKBOOK = load_workbook(filename="C:/Users/joaov/Downloads/Eu.xlsx")


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
