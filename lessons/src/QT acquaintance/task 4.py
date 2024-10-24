import sys

from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QLineEdit, QGridLayout


class WidgetsHideNSeek(QWidget):
    condition = {
        0: True,
        1: True,
        2: True,
        3: True,
    }
    inputs_text = {}

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Миникалькулятор')
        self.__init_component()
        self.__show_component()

        self.adjustSize()

    def __init_component(self):
        self.edit1 = QLineEdit(self)
        self.edit2 = QLineEdit(self)
        self.edit3 = QLineEdit(self)
        self.edit4 = QLineEdit(self)
        self.inputs_text[0] = self.edit1
        self.inputs_text[1] = self.edit2
        self.inputs_text[2] = self.edit3
        self.inputs_text[3] = self.edit4

        self.checkbox1 = QCheckBox(self)
        self.checkbox2 = QCheckBox(self)
        self.checkbox3 = QCheckBox(self)
        self.checkbox4 = QCheckBox(self)

        self.checkbox1.setText('edit1')
        self.checkbox2.setText('edit2')
        self.checkbox3.setText('edit3')
        self.checkbox4.setText('edit4')

        self.checkbox1.clicked.connect(lambda: self.onclick(0))
        self.checkbox2.clicked.connect(lambda: self.onclick(1))
        self.checkbox3.clicked.connect(lambda: self.onclick(2))
        self.checkbox4.clicked.connect(lambda: self.onclick(3))


    def __show_component(self):
        loyout = QGridLayout()
        loyout.addWidget(self.checkbox1, 0, 0)
        loyout.addWidget(self.checkbox2, 1, 0)
        loyout.addWidget(self.checkbox3, 2, 0)
        loyout.addWidget(self.checkbox4, 3, 0)

        for key, val in self.inputs_text.items():
            loyout.addWidget(val, key, 1)

        self.setLayout(loyout)

    def onclick(self, position):
        self.condition[position] = not self.condition[position]

        if self.condition[position]:
            self.inputs_text[position].show()
        else:
            self.inputs_text[position].hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    evaluator = WidgetsHideNSeek()
    evaluator.show()

    sys.exit(app.exec())