import sys
import random
from PyQt6 import QtWidgets, QtGui, QtCore


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Случайные окружности")
        MainWindow.resize(600, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton = QtWidgets.QPushButton("Добавить окружность", self.centralwidget)
        self.pushButton.setGeometry(10, 10, 200, 40)  # координаты и размер кнопки


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.circles = []

        self.ui.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(20, 120)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)

        color = QtGui.QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)

        for x, y, d, color in self.circles:
            painter.setBrush(QtGui.QBrush(color))
            painter.setPen(QtGui.QPen(color))
            painter.drawEllipse(x, y, d, d)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
