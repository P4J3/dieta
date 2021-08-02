# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dieta.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

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
        'bisteca':{'id': 15, 'nome': 'Bisteca Bovina', 'calorias': 291, 'proteina': 30.1, 'carboidratos': 0},
        'abacate':{'id': 16, 'nome': 'Abacate', 'calorias': 160, 'proteina': 2, 'carboidratos': 8.53},
        'bistaca_porco':{'id': 17, 'nome': 'Bisteca de Porco', 'calorias': 279, 'proteina': 26.41, 'carboidratos': 0},
        'fecula':{'id': 18, 'nome': 'Fécula', 'calorias': 360, 'proteina': 0, 'carboidratos': 90},
        'aveia':{'id': 19, 'nome': 'Aveia', 'calorias': 390, 'proteina': 16.67, 'carboidratos': 53.33},
}

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(575, 312)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendario = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendario.setGeometry(QtCore.QRect(165, 11, 312, 161))
        self.calendario.setObjectName("calendario")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 11, 137, 205))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelAlimento = QtWidgets.QLabel(self.widget)
        self.labelAlimento.setObjectName("labelAlimento")
        self.verticalLayout_3.addWidget(self.labelAlimento)
        self.comboAlimento = QtWidgets.QComboBox(self.widget)
        self.comboAlimento.setObjectName("comboAlimento")
        for chave, valor in lista_alimentos.items():
            self.comboAlimento.insertItem(valor['id'], valor['nome'])

        self.verticalLayout_3.addWidget(self.comboAlimento)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelRefeicao = QtWidgets.QLabel(self.widget)
        self.labelRefeicao.setObjectName("labelRefeicao")
        self.verticalLayout_2.addWidget(self.labelRefeicao)
        self.comboRefeicao = QtWidgets.QComboBox(self.widget)
        self.comboRefeicao.setObjectName("comboRefeicao")
        self.comboRefeicao.addItem("")
        self.comboRefeicao.addItem("")
        self.comboRefeicao.addItem("")
        self.comboRefeicao.addItem("")
        self.comboRefeicao.addItem("")
        self.comboRefeicao.addItem("")
        self.verticalLayout_2.addWidget(self.comboRefeicao)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelQuantidade = QtWidgets.QLabel(self.widget)
        self.labelQuantidade.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.labelQuantidade.setObjectName("labelQuantidade")
        self.verticalLayout.addWidget(self.labelQuantidade)
        self.inputQuantidade = QtWidgets.QLineEdit(self.widget)
        self.inputQuantidade.setObjectName("inputQuantidade")
        self.verticalLayout.addWidget(self.inputQuantidade)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(464, 195, 91, 81))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.botaoInserirAlimento = QtWidgets.QPushButton(self.widget1)
        self.botaoInserirAlimento.setObjectName("botaoInserirAlimento")
        self.verticalLayout_6.addWidget(self.botaoInserirAlimento)
        self.botaoSalvarRefeicao = QtWidgets.QPushButton(self.widget1)
        self.botaoSalvarRefeicao.setObjectName("botaoSalvarRefeicao")
        self.verticalLayout_6.addWidget(self.botaoSalvarRefeicao)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(196, 201, 161, 16))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelTotalCalorias = QtWidgets.QLabel(self.widget2)
        self.labelTotalCalorias.setObjectName("labelTotalCalorias")
        self.horizontalLayout.addWidget(self.labelTotalCalorias)
        self.outputCalorias = QtWidgets.QLabel(self.widget2)
        self.outputCalorias.setText("")
        self.outputCalorias.setObjectName("outputCalorias")
        self.horizontalLayout.addWidget(self.outputCalorias)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(196, 258, 161, 22))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelTotalProteinas = QtWidgets.QLabel(self.widget3)
        self.labelTotalProteinas.setObjectName("labelTotalProteinas")
        self.horizontalLayout_3.addWidget(self.labelTotalProteinas)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.outputProteinas = QtWidgets.QLabel(self.widget3)
        self.outputProteinas.setText("")
        self.outputProteinas.setObjectName("outputProteinas")
        self.horizontalLayout_3.addWidget(self.outputProteinas)
        self.widget4 = QtWidgets.QWidget(self.centralwidget)
        self.widget4.setGeometry(QtCore.QRect(196, 229, 161, 16))
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelTotalCarboidratos = QtWidgets.QLabel(self.widget4)
        self.labelTotalCarboidratos.setObjectName("labelTotalCarboidratos")
        self.horizontalLayout_2.addWidget(self.labelTotalCarboidratos)
        self.outputCarboidratos = QtWidgets.QLabel(self.widget4)
        self.outputCarboidratos.setText("")
        self.outputCarboidratos.setObjectName("outputCarboidratos")
        self.horizontalLayout_2.addWidget(self.outputCarboidratos)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dieta"))
        self.labelAlimento.setText(_translate("MainWindow", "Alimento"))
        self.labelRefeicao.setText(_translate("MainWindow", "Refeição"))
        self.comboRefeicao.setItemText(0, _translate("MainWindow", "Café"))
        self.comboRefeicao.setItemText(1, _translate("MainWindow", "Almoço"))
        self.comboRefeicao.setItemText(2, _translate("MainWindow", "Tarde"))
        self.comboRefeicao.setItemText(3, _translate("MainWindow", "Jantar"))
        self.comboRefeicao.setItemText(4, _translate("MainWindow", "Pós-Jantar"))
        self.comboRefeicao.setItemText(5, _translate("MainWindow", "Pós-Treino"))
        self.labelQuantidade.setText(_translate("MainWindow", "Quantidade:"))
        self.botaoInserirAlimento.setText(_translate("MainWindow", "Inserir Alimento"))
        self.botaoSalvarRefeicao.setText(_translate("MainWindow", "Salvar Refeição"))
        self.labelTotalCalorias.setText(_translate("MainWindow", "Total Calorias:"))
        self.labelTotalProteinas.setText(_translate("MainWindow", "Total Proteínas:"))
        self.labelTotalCarboidratos.setText(_translate("MainWindow", "Total Carboidratos:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
