from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
import sys
from calculadora_dieta.dieta import Ui_MainWindow
from pprint import pprint
from calculadora_dieta.calcula_calorias_v3 import calorias_macros
from calculadora_dieta.grava_macros_v2 import salva_tudo
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

        alimento = self.comboAlimento.currentIndex() + 1
        print(alimento)
        #print(self.comboAlimento.currentIndex())

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
        macros = {'Calorias': self.total_calorias, 'Proteína': self.total_proteinas, 'Carboidratos': self.total_carboidratos}
        dia = self.calendario.selectedDate().day()
        refeicao = self.comboRefeicao.currentText()
        #k = datetime.strptime(dia,'%d/%m/%Y')
        print(f'Dia:{dia}')
        for chave, valor in macros.items():
            salva_tudo(valor, chave, refeicao, dia)
        self.total_calorias = 0
        self.total_proteinas = 0
        self.total_carboidratos = 0

        self.outputCalorias.setText(f'{self.total_calorias:.2f}g')
        self.outputCarboidratos.setText(f'{self.total_carboidratos:.2f}g')
        self.outputProteinas.setText(f'{self.total_proteinas:.2f}g')

    def zerar(self):
        self.total_proteinas = 0
        self.total_calorias = 0
        self.total_carboidratos = 0

def window():
    app = QApplication(sys.argv)
    win = Aplicativo()
    win.show()
    sys.exit(app.exec())


window()