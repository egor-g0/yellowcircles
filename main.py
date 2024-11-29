import sys
from random import randint

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QWidget, QApplication


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('01.ui', self)  # Загружаем дизайн
        self.circles = []
        self.pushButton.clicked.connect(self.add)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_circles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for circle in self.circles:
            x, y, r = circle
            qp.drawEllipse(QPoint(x, y), r, r)


    def add(self):
        r = randint(10, 50)
        x = randint(50, 550)
        y = randint(50, 550)
        self.circles.append((x, y, r))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
