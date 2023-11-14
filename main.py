import random
import sys
import io
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit


class Square1(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(open('UI.ui', encoding='utf8').read())
        uic.loadUi(f, self)
        self.color = QColor(255, 255, 0)
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self)
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.update()
        self.repaint()

    def draw_flag(self, qp):
        qp.setPen(self.color)
        qp.setBrush(QColor(255, 255, 0))
        d = random.randint(10, 250)
        qp.drawEllipse(random.randint(0, 500), random.randint(0, 350), d, d)

    def except_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square1()
    ex.show()
    sys.excepthook = ex.except_hook
    sys.exit(app.exec())
