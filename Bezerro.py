from PyQt5 import  uic,QtWidgets
import sqlite3

app=QtWidgets.QApplication([])
tela_bezerro=uic.loadUi("tela_bezerro.ui")

tela_bezerro.show()
app.exec()