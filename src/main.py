from cgitb import reset
import sys

from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from ui.Ui_calculator import *
from util.calculator import *


class DialogoCalculatorAplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Calculadora")

        # Incialmente se desactiva los operadores, el igual y el AC
        self.deactivate_operators()
        self.deactivate_equal()
        self.deactivate_ac()

        self.ui.lineEdit_in_out.textEdited.connect(self.on_text_edited)

        self.operation = ''
        self.a = 0
        self.b = 0
        self.operator = ''
        self.result = 0
        self.is_a = False
        self.is_b = False
        self.is_operator = False

        self.ui.pushButton_0.clicked.connect(self.on_0_clicked)
        self.ui.pushButton_1.clicked.connect(self.on_1_clicked)
        self.ui.pushButton_2.clicked.connect(self.on_2_clicked)
        self.ui.pushButton_3.clicked.connect(self.on_3_clicked)
        self.ui.pushButton_4.clicked.connect(self.on_4_clicked)
        self.ui.pushButton_5.clicked.connect(self.on_5_clicked)
        self.ui.pushButton_6.clicked.connect(self.on_6_clicked)
        self.ui.pushButton_7.clicked.connect(self.on_7_clicked)
        self.ui.pushButton_8.clicked.connect(self.on_8_clicked)
        self.ui.pushButton_9.clicked.connect(self.on_9_clicked)
        self.ui.pushButton_add.clicked.connect(self.on_add_clicked)
        self.ui.pushButton_substract.clicked.connect(self.on_substract_clicked)
        self.ui.pushButton_multiply.clicked.connect(self.on_multiply_clicked)
        self.ui.pushButton_divide.clicked.connect(self.on_divide_clicked)
        self.ui.pushButton_ac.clicked.connect(self.on_ac_clicked)
        self.ui.pushButton_equal.clicked.connect(self.on_equal_clicked)
        self.ui.pushButton_info.clicked.connect(self.on_info_clicked)

    def update_operation(self, n_or_o):
        self.operation += n_or_o
        self.ui.lineEdit_in_out.setText(self.operation)
        if len(self.operation) > 0:
            self.activate_ac()

        if len(self.operation) == 1:
            self.activate_operators()

        if self.is_a and self.is_operator and self.operation.split(' ')[-1] != '':
            self.is_b = True

        if self.is_a and self.is_b and self.is_operator:
            self.activate_equal()

    def on_0_clicked(self):
        self.update_operation('0')

    def on_1_clicked(self):
        self.update_operation('1')

    def on_2_clicked(self):
        self.update_operation('2')

    def on_3_clicked(self):
        self.update_operation('3')

    def on_4_clicked(self):
        self.update_operation('4')

    def on_5_clicked(self):
        self.update_operation('5')

    def on_6_clicked(self):
        self.update_operation('6')

    def on_7_clicked(self):
        self.update_operation('7')

    def on_8_clicked(self):
        self.update_operation('8')

    def on_9_clicked(self):
        self.update_operation('9')

    def on_add_clicked(self):
        self.operator_selected('+')
        self.update_operation(' + ')

    def on_substract_clicked(self):
        self.operator_selected('-')
        self.update_operation(' - ')

    def on_multiply_clicked(self):
        self.operator_selected('*')
        self.update_operation(' * ')

    def on_divide_clicked(self):
        self.operator_selected('/')
        self.update_operation(' / ')

    def on_info_clicked(self):
        msg = "Calculadora básica para sumar, restar, multiplicar y dividir.\n\nRealizado por: Danilo Mendoza\nGitHub: https://github.com/odmendoza/python-pyqt5-calculator\n"
        QMessageBox.about(self, "Información", msg)

    def operator_selected(self, operator):
        self.deactivate_operators()
        print(self.operation.split(' ')[0])
        self.a = int(self.operation.split(' ')[0])
        self.is_a = True
        self.operator = operator
        self.is_operator = True

    def on_equal_clicked(self):
        self.b = int(self.operation.split(' ')[-1])

        result = 0

        if self.operator == '+':
            result = add(self.a, self.b)
        if self.operator == '-':
            result = substract(self.a, self.b)
        if self.operator == '*':
            result = multiply(self.a, self.b)
        if self.operator == '/':
            result = divide(self.a, self.b)
            if result == None:
                result = 'No es posible la división para cero'
                self.deactivate_operators()

        self.ui.lineEdit_in_out.setText(str(result))
        self.deactivate_numbers()
        self.deactivate_equal()

    def on_ac_clicked(self):
        self.operation = ''
        self.ui.lineEdit_in_out.setText('')
        self.deactivate_operators()
        self.deactivate_ac()
        self.deactivate_equal()
        self.activate_numbers()

    def on_text_edited(self):
        cleaned_text = self.ui.lineEdit_in_out.text()[:-1]
        self.ui.lineEdit_in_out.setText(cleaned_text)

    def deactivate_numbers(self):
        self.ui.pushButton_0.setDisabled(True)
        self.ui.pushButton_1.setDisabled(True)
        self.ui.pushButton_2.setDisabled(True)
        self.ui.pushButton_3.setDisabled(True)
        self.ui.pushButton_4.setDisabled(True)
        self.ui.pushButton_5.setDisabled(True)
        self.ui.pushButton_6.setDisabled(True)
        self.ui.pushButton_7.setDisabled(True)
        self.ui.pushButton_8.setDisabled(True)
        self.ui.pushButton_9.setDisabled(True)

    def activate_numbers(self):
        self.ui.pushButton_0.setDisabled(False)
        self.ui.pushButton_1.setDisabled(False)
        self.ui.pushButton_2.setDisabled(False)
        self.ui.pushButton_3.setDisabled(False)
        self.ui.pushButton_4.setDisabled(False)
        self.ui.pushButton_5.setDisabled(False)
        self.ui.pushButton_6.setDisabled(False)
        self.ui.pushButton_7.setDisabled(False)
        self.ui.pushButton_8.setDisabled(False)
        self.ui.pushButton_9.setDisabled(False)

    def deactivate_operators(self):
        self.ui.pushButton_add.setDisabled(True)
        self.ui.pushButton_substract.setDisabled(True)
        self.ui.pushButton_multiply.setDisabled(True)
        self.ui.pushButton_divide.setDisabled(True)

    def activate_operators(self):
        self.ui.pushButton_add.setDisabled(False)
        self.ui.pushButton_substract.setDisabled(False)
        self.ui.pushButton_multiply.setDisabled(False)
        self.ui.pushButton_divide.setDisabled(False)

    def deactivate_equal(self):
        self.ui.pushButton_equal.setDisabled(True)

    def activate_equal(self):
        self.ui.pushButton_equal.setDisabled(False)

    def deactivate_ac(self):
        self.ui.pushButton_ac.setDisabled(True)

    def activate_ac(self):
        self.ui.pushButton_ac.setDisabled(False)


if __name__ == '__main__':
    # Crea entorno de tipo QApplication y pasa como parámetro las lista de parametros, linea de comandos
    app = QApplication(sys.argv)

    # Crea dialogo
    ui = DialogoCalculatorAplicacion()

    # Muestra el dialogo
    ui.show()
    
    # Para el evento de salida, invocamos el método exec.
    sys.exit(app.exec_())
