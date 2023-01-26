#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)

        self.setWindowTitle('Python_lab4.2_MAS10')

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)

    def solve(self):
        self.textEdit_words.clear()
        text = self.textEdit_text.toPlainText().split()

        count = 0
        itog = ""

        for word in text:
            word_changecase = str(word).casefold()
            if word_changecase.startswith("а") and word_changecase.endswith("я"):
                count += 1
                itog += (word + ", ")
        itog = itog[:-2]
        self.textEdit_words.insertPlainText("Количество нужных слов = " + str(count) + "\n")
        self.textEdit_words.insertPlainText(itog)


    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
