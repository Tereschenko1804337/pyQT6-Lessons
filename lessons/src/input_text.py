from PyQt6.QtWidgets import QLineEdit, QWidget


class InputTextWidget(QLineEdit):
    def __init__(self, form: QWidget):
        super().__init__(form)

        self.form = form
        self.__initUI()


    def __initUI(self):
        center_width = int(self.form.width() / 2) - int(self.width() / 2)

        self.setFixedWidth(100)
        self.move(center_width, 100)
