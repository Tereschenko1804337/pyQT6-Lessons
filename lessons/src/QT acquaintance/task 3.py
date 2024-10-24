import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QLCDNumber


class MiniCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Миникалькулятор')
        self.__init_component()
        self.__show_component()

        self.adjustSize()

    def __init_component(self):
        self.first_number_text = QLabel("Первое число(целое):")
        self.second_number_text = QLabel("Второе число(целое):")

        self.result_amount_text = QLabel("Сумма:")
        self.result_difference_text = QLabel("Разность:")
        self.result_product_text = QLabel("Произведение:")
        self.result_quotient_text = QLabel("Частное:")

        self.number_1 = QLineEdit(self)
        self.number_2 = QLineEdit(self)

        self.calculate_button = QPushButton(self)
        self.calculate_button.setText('->')
        self.calculate_button.clicked.connect(self.onclick)

        self.result_sum = QLCDNumber(self)
        self.result_sub = QLCDNumber(self)
        self.result_mul = QLCDNumber(self)
        self.result_div = QLCDNumber(self)


    def __show_component(self):
        right_loyout = QGridLayout()
        right_loyout.addWidget(self.result_amount_text, 0, 0)
        right_loyout.addWidget(self.result_difference_text, 1, 0)
        right_loyout.addWidget(self.result_product_text, 2, 0)
        right_loyout.addWidget(self.result_quotient_text, 3, 0)
        right_loyout.addWidget(self.result_sum, 0, 1)
        right_loyout.addWidget(self.result_sub, 1, 1)
        right_loyout.addWidget(self.result_mul, 2, 1)
        right_loyout.addWidget(self.result_div, 3, 1)

        left_loyout = QGridLayout()
        left_loyout.addWidget(self.first_number_text, 0, 0)
        left_loyout.addWidget(self.number_1, 1, 0)
        left_loyout.addWidget(self.second_number_text, 2, 0)
        left_loyout.addWidget(self.number_2, 3, 0)

        main_layout = QGridLayout()
        main_layout.addLayout(left_loyout, 0, 0)
        main_layout.addWidget(self.calculate_button, 0, 1)
        main_layout.addLayout(right_loyout, 0, 2)

        self.setLayout(main_layout)
        self.__show_lcd_result()


    def onclick(self):
        number_1 = self.number_1.text()
        number_2 = self.number_2.text()
        amount = int(number_1) + int(number_2)
        difference = int(number_1) - int(number_2)
        product = int(number_1) * int(number_2)
        quotient = "Error"
        if int(number_2):
            quotient = int(number_1) / int(number_2)

        self.__show_lcd_result(amount, difference, product, quotient)
        self.__show_component()


    def __show_lcd_result(self, amount=0, difference=0, product=0, quotient=0):
        self.result_sum.display(f'{amount}')
        self.result_sub.display(f'{difference}')
        self.result_mul.display(f'{product}')
        self.result_div.display(f'{quotient}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    evaluator = MiniCalculator()
    evaluator.show()

    sys.exit(app.exec())