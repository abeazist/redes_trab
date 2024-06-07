import sys
import PyQt5.QtWidgets


class Principal(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        layout = PyQt5.QtWidgets.QGridLayout()

        self.setLayout(layout)

def main():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    janela = Principal()
    janela.show()
    app.exec()


if __name__ == '__main__':
    main()
