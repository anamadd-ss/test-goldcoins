#Convert the resulting py file
from GoldCoins import Ui_TelaInicial
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import resources

#Inherited to the main window class of the interface file
class MainWindow(QMainWindow, Ui_TelaInicial):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec())

