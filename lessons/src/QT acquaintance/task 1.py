import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QHBoxLayout


class MainWindow(QWidget):
    to_right = True
    btn_text = {
        True: '->',
        False: '<-'
    }

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Фокус со словами')
        layout = QHBoxLayout()

        self.left_text_input = QLineEdit(self)
        self.right_text_input = QLineEdit(self)

        self.button = QPushButton(self)
        self.button.setText(self.btn_text[self.to_right])
        self.button.clicked.connect(self.onclick)

        layout.addWidget(self.left_text_input)
        layout.addWidget(self.button)
        layout.addWidget(self.right_text_input)

        self.setLayout(layout)
        self.adjustSize()


    def onclick(self):
        if self.to_right:
            self.right_text_input.setText(self.left_text_input.text())
            self.left_text_input.clear()
        else:
            self.left_text_input.setText(self.right_text_input.text())
            self.right_text_input.clear()

        self.to_right = not self.to_right
        self.button.setText(self.btn_text[self.to_right])


# class TextInput(QLineEdit):
#     def __init__(self, form: QWidget):
#         super().__init__(form)
#         self.initUI()
#
#     def initUI(self):
#         ...


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())