import sys

from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

from input_text import InputTextWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def __set_center_screen(self):
        cursor_pos = QCursor.pos()
        active_screen = None
        for screen in QApplication.screens():
            if screen.geometry().contains(cursor_pos):
                active_screen = screen
                break

        screen_geometry = active_screen.availableGeometry()

        # TODO: Потом включить для центрирования
        # x = (screen_geometry.width() - self.width()) // 2 + screen_geometry.x()
        x = (screen_geometry.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2 + screen_geometry.y()
        self.move(x, y)

    def initUi(self):
        self.setFixedSize(300, 500)
        self.setWindowTitle('Перая прога')

        self.__set_center_screen()
        self.__set_interface()

    def __set_interface(self):
        self.btn = QPushButton('Ввод', self)
        # Подстроим размер кнопки под надпись на ней
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 150)
        # Обратите внимание: функцию не надо вызывать
        self.btn.clicked.connect(self.inc_click)

        self.text_input = InputTextWidget(self)

    def inc_click(self):
        text = self.text_input.text()
        self.text_input.clear()
        self.text_input.setPlaceholderText(text)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()

    form.show()

    sys.exit(app.exec())