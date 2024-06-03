import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QTableWidget, QErrorMessage, QTimeEdit
from PyQt5.QtCore import QTimer, QTime
from sqlite3 import Cursor
from PyQt5.uic import loadUi
import mysql
import mysql.connector
from mysql.connector import Error
import mysql.connector
from tkinter import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from datetime import datetime
import time
from datetime import datetime
import threading
import PyInstaller.__main__
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build

app = QtWidgets.QApplication([])
# conexão com banco de dados
banco = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    password = '123456',
    database = 'cat_treinee'
)

# google search
api_key = "AIzaSyAHuFEjZ8bNx9jPmKp5rMd9lVs3xRqqluk"
cse_id = f"5049fa9938f704a81"
query = "a decidir"

# declaração das telas
cadastros = uic.loadUi('telas\cadastros.ui')
inicial = uic.loadUi('telas\inicial_cat.ui')
login = uic.loadUi('telas\login_cat.ui')

# iniciar aplicativo
login.show()
app.exec_()