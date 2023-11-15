import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPolygonF
from PyQt5.QtWidgets import QColorDialog


class Square2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1000, 1000)

        self.draw = QPushButton(self)
        self.draw.move(300, 10)
        self.draw.setText("Рисовать")
        self.draw.clicked.connect(self.paint)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.paint(qp)
        qp.end()

    def paint(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        a = random.randint(0, 1000)
        qp.drawEllipse(0, 0, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square2()
    ex.show()
    exit(app.exec())