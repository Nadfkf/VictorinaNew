import sys
import random
import json
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QLineEdit,QFrame,QRadioButton


data ={"name": "Превед Медвед","answers": ["От Джона Лури","От Бебры","Из Майнкрафта"]}
# главное окно приложения расширяет класс QWidget
class MainWidget(QFrame,QVBoxLayout):
    # список предложений
    strings = ["Перестань Щелкать", "Тестируй Это приложение!!!!!!",":D"]
    def show_new_window(self):
        #self.hide()
        self.button3.hide()
        self.text.hide()
        self.w = AnotherWindow()
        self.layout.addWidget(self.w)
        #self.w.resize(800, 600)
       
    # конструктор 
    def __init__(self):
        super().__init__()
        
        self.button3 = QPushButton("Нажмите чтобы начать тестировать!")
        # создаем текстовую метку отцентиророванную посередине контейнера
        self.text = QLabel("Привет,Это Тест на знание происхождения мемов", alignment=Qt.AlignCenter)
     
        # вертикальная разметка
        self.layout = QVBoxLayout(self)
        # добавляем виджеты в разметку
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button3)
        # назначаем обработчки для копки на событие клика
        self.button3.clicked.connect(self.show_new_window)
    # сам обработчик
     
class AnotherWindow(QFrame,QVBoxLayout,QWidget):
    
    def show_new_window(self):
        #self.hide()
        self.text.hide()
        self.button4.hide()
        self.button5.hide()
        self.radiobutton.hide()
        self.radiobutton2.hide()
        self.radiobutton3.hide()
        self.w = MainWidget()
        self.layout.addWidget(self.w)
        #self.w.resize(800, 600)
    def show_newnew_window(self):
        #self.hide()
        self.text.hide()
        self.button4.hide()
        self.button5.hide()
        self.radiobutton.hide()
        self.radiobutton2.hide()
        self.radiobutton3.hide()
        self.w = AnotherWindow()
        self.layout.addWidget(self.w)
        #self.w.resize(800, 600)
        
    def __init__(self):
        super().__init__()
        question = data["name"]
        answers = data["answers"]
        self.text = QLabel(question, alignment=Qt.AlignCenter)
        self.layout = QVBoxLayout(self)
        self.radiobutton = QRadioButton(answers[0])
        self.radiobutton2 = QRadioButton(answers[1])
        self.radiobutton3 = QRadioButton(answers[2])
        self.button4 = QPushButton("Вернуться обратно")
        self.button5 = QPushButton("Перейти на другой фрейм")
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.radiobutton)
        self.layout.addWidget(self.radiobutton2)
        self.layout.addWidget(self.radiobutton3)
        self.layout.addWidget(self.button4)
        self.layout.addWidget(self.button5)
        self.button4.clicked.connect(self.show_new_window)
        self.button5.clicked.connect(self.show_newnew_window)
if __name__ == "__main__":
    # главный класс приложения принимает строку - заголовок окна
    app = QApplication(['Пример прииложения на PyQT'])

    # создаем главный виджет размером 800x600 и отображаем его
    widget = MainWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
