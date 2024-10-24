import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout


class Evaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Вычисление выражений')
        self.__init_component()
        self.__show_component()

        self.adjustSize()

    def __init_component(self):
        self.expression_label = QLabel("Выражение:")
        self.result_label = QLabel("Результат:")

        self.first_value = QLineEdit(self)
        self.second_value = QLineEdit(self)

        self.trick_button = QPushButton(self)
        self.trick_button.setText('->')
        self.trick_button.clicked.connect(self.onclick)


    def __show_component(self):
        layout = QGridLayout()

        layout.addWidget(self.expression_label, 0, 0)
        layout.addWidget(self.result_label, 0, 2)
        layout.addWidget(self.first_value, 1, 0)
        layout.addWidget(self.trick_button, 1, 1)
        layout.addWidget(self.second_value, 1, 2)

        self.setLayout(layout)



    def onclick(self):
        text = self.first_value.text()
        result = eval(text)
        self.second_value.setText(f'{result}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    evaluator = Evaluator()
    evaluator.show()

    sys.exit(app.exec())