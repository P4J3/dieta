from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
import sys
from tools.dieta import Ui_MainWindow
from pprint import pprint
from tools.tools import calorias_macros, salva_tudo
from datetime import datetime

class Aplicativo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        #super().comboAlimentos.insertItem(0,'Primeiro')
        self.total_calorias = 0
        self.total_proteinas = 0
        self.total_carboidratos = 0
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.botaoInserirAlimento.clicked.connect(self.calcula_refeicao)
        self.botaoSalvarRefeicao.clicked.connect(self.salva)

    def calcula_refeicao(self):

        alimento = self.comboAlimento.currentIndex() + 1 # Pega o alimento escolhido pelo usuário
        print(alimento)
        #print(self.comboAlimento.currentIndex())

        '''
            Pega a quantidade digitada pelo usuário e a tranforma em um número inteiro
        '''
        quantidade_atual = self.inputQuantidade.text() 
        quantidade_atual = int(quantidade_atual)

        print(calorias_macros(alimento, quantidade_atual))

        '''
            Pega as calorias e os macros do alimento
        '''
        dicionario_alimento = calorias_macros(alimento, quantidade_atual)
        calorias = dicionario_alimento['calorias']
        proteinas = dicionario_alimento['proteinas']
        carboidratos = dicionario_alimento['carboidratos']

        '''
            Soma o total de calorias e macros da refeição
        '''
        self.total_calorias +=calorias
        self.total_proteinas +=proteinas
        self.total_carboidratos +=carboidratos

        print(self.total_calorias)

        '''
            Mostra para o usuário as calorias e os macros da refeição
        '''
        self.outputCalorias.setText(f'{self.total_calorias:.2f}g')
        self.outputCarboidratos.setText(f'{self.total_carboidratos:.2f}g')
        self.outputProteinas.setText(f'{self.total_proteinas:.2f}g')


        #self.total.setText(str(self.valor_total)+'g')

    def salva(self):
        # Cria um dic que armazena os valores das calorias das proteínas e dos carbo
        macros = {'Calorias': self.total_calorias, 'Proteína': self.total_proteinas, 'Carboidratos': self.total_carboidratos}

        dia = self.calendario.selectedDate().day() # Pega o dia selecionado pelo usuário
        refeicao = self.comboRefeicao.currentText() # Pega refeição selecionada pelo usuário
        print(refeicao)
        #k = datetime.strptime(dia,'%d/%m/%Y')
        print(f'Dia:{dia}')
        '''
            Para cada valor no dic macros:
                +Chama a função salva_tudo que recebe como parâmetro
                    +A quantidade de macros ou calorias
                    +O nome da chave que deve ser igual ao nome da woorksheet do excel(Calorias, Proteína e Carbodratos)
                    +O nome da refeição
                    +O dia escolhido pelo usuário
        '''
        for chave, valor in macros.items():
            salva_tudo(valor, chave, refeicao, dia)
        
        '''
            Depois de salvar, zera os valores para outra refeição ser adicionada
        '''    
        self.total_calorias = 0
        self.total_proteinas = 0
        self.total_carboidratos = 0

        '''
            Muda os valores dos outputs para zero
        '''
        self.outputCalorias.setText(f'{self.total_calorias:.2f}gSS')
        self.outputCarboidratos.setText(f'{self.total_carboidratos:.2f}g')
        self.outputProteinas.setText(f'{self.total_proteinas:.2f}g')

    #TODO: O botão que chamaria essa função ainda deve ser adicionado na interface
    def zerar(self):
        self.total_proteinas = 0
        self.total_calorias = 0
        self.total_carboidratos = 0


def window():
    app = QApplication(sys.argv) # Cria a aplicação
    win = Aplicativo() # Instancia a classe
    win.show() # Mostra a classe na aplicaçãos
    sys.exit(app.exec()) # Que ao aperta o X a aplicação será encerrada


window()
