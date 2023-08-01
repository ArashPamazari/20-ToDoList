from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from functools import partial
# toozihat Ui
"""""
grid layout 
3 textlabel , task 1 , task 2 , task 3
3 checkbox

dar paeen safhe yek harizontal layout
2 line edit  : title and descriptions
1 push button

dar ghesmat khali page > right click : layout vertical

vertical policy : minimum 
save at path with name of mainwindow.ui

3 file : db , py , ui

"""

"""""
read ui file and load it
read info in database and show in ui file
and add new tasks in ui and add in database

"""


#import sqlite3
import database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('mainwindow.ui', None)
        self.ui.show()

        
        self.readFromDatabase()
        self.ui.btn_add.clicked.connect(self.addNewTaskToDatabase)
    


    def readFromDatabase(self): #read from database to add ui
        
        #connection = sqlite3.connect('database.db')
        #my_cursor = connection.cursor()

        #my_cursor.execute('SELECT * FROM tasks')
        #results = my_cursor.fetchall()
        
        results = database.getAll()

        for i in range(len(results)): # Choon taskHa hey Ezafe mishan
            
            new_checkbox = QCheckBox() #need checkbox from Class of QCheckBox            
            
            new_label = QLabel() #need label from Class of Qlabel 
            new_label.setText(results[i][1]) #esme task
            #self.ui.gridLayout.addWidget(new_label,i,1) # make at Ui

            new_info_button = QPushButton()
            new_info_button.setText('info')
           

            new_delete_button = QPushButton()
            new_delete_button.setText('🗑')
            #self.ui.gridLayout.addWidget(new_delete_button,i,2)


            new_priority_button = QPushButton()

            
                        
            
            
            if results[i][3]==1:    #result i om , andis 3 omesh = 1 bud yani Done shode 
                new_checkbox.setChecked(True)
            self.ui.gridLayout.addWidget(new_checkbox,i,0) # make at Ui


            if results[i][3] == 0 :
                self.ui.gridLayout.addWidget(new_priority_button, i, 0)
                self.ui.gridLayout.addWidget(new_info_button, i, 1)
                
                self.ui.gridLayout.addWidget(new_label, i, 2)
                self.ui.gridLayout.addWidget(new_checkbox, i, 3)
                
                self.ui.gridLayout.addWidget(new_delete_button, i, 4)

            elif results[i][3] == 1:
                self.ui.gridLayout1.addWidget(new_priority_button, i, 0)
                self.ui.gridLayout1.addWidget(new_info_button, i, 1)
                self.ui.gridLayout1.addWidget(new_label, i, 2)
                self.ui.gridLayout1.addWidget(new_checkbox, i, 3)
                self.ui.gridLayout1.addWidget(new_delete_button, i, 4)






            if results[i][6] == 0:
                new_priority_button.setText('🏳')
                new_label.setStyleSheet('background-color: rgb(240, 240, 240);font: 700 9pt "Segoe UI"')
            
            elif results[i][6] == 1:
                new_priority_button.setText('📌')
                new_label.setStyleSheet('background-color: red;font: 700 9pt "Segoe UI"')

            new_checkbox.setStyleSheet('max-width: 30px; min-height: 30px')
            new_delete_button.setStyleSheet('background-color: white;max-width: 35px; min-height: 30px; font: 700 9pt "Segoe UI";')
            new_priority_button.setStyleSheet('background-color:white;max-width: 35px; min-height: 30px;font: 700 9pt "Segoe UI";')
            
            new_info_button.setStyleSheet('background-color: white;max-width: 35px; min-height: 30px;font: 700 9pt "Black UI";')

            new_checkbox.clicked.connect(partial(self.DoneToDataBase, new_checkbox, new_label, new_delete_button, results[i][1], new_info_button, new_priority_button))
            new_delete_button.clicked.connect(partial(self.DelTasksatDatabase,new_checkbox, new_label, new_delete_button, results[i][1], new_info_button, new_priority_button))
            new_priority_button.clicked.connect(partial(self.priority, results[i][6], results[i][1]))
            new_info_button.clicked.connect(partial(self.info, results[i][2], results[i][4], results[i][5]))






    def addNewTaskToDatabase(self):   #read info from textbox and insert to table task
            title = self.ui.tb_title.text()
            description = self.ui.tb_description.text()
            time = self.ui.tb_time.text()
            date = self.ui.tb_date.text()
            id = len(database.getAll()) + 1

            #connection = sqlite3.connect('database.db')
            #my_cursor = connection.cursor()

            #my_cursor.execute(f'INSERT INTO tasks(title , description) VALUES("{title}","{description}")') # baray inke vasat string , variable bezarim aval string f mizarim
            #connection.commit()
            database.add(id, title, description, time, date)

            self.readFromDatabase() # dobare etelAt ro bekhon va be ui ezafe kon

            self.ui.tb_title.setText('') # Clear and make ready for new task
            self.ui.tb_description.setText('') # Clear and make ready for new description
            self.ui.tb_time.setText('')
            self.ui.tb_date.setText('')                 




    def DoneToDataBase(self, check, label, delete, title, info, prio):
        if check.isChecked():
            database.updateDoneTasks(1, title)
        else:
            database.updateDoneTasks(0, title)
        check.deleteLater()
        label.deleteLater()
        delete.deleteLater()
        info.deleteLater()
        prio.deleteLater()
        self.readFromDatabase()

    def DelTasksatDatabase(self,checkbox, label, delete, title, info, prio):
        database.deleteTasks(title)
        checkbox.deleteLater()
        label.deleteLater()
        delete.deleteLater()
        info.deleteLater()
        prio.deleteLater()

    def priority(self, prio, title):
        if prio == 0:
            database.priorityFunc(1, title)
        elif prio == 1:
            database.priorityFunc(0, title)
        self.readFromDatabase()

    def info(self, description, time, date):
        msgBox = QMessageBox()
        msgBox.setText(description+ ' , '+ time+ ' , '+ date)
        msgBox.exec()


app = QApplication([])
window = MainWindow()
app.exec_()



# qt application graphics
# arcade game
# telegram bot
# sheygaraeee
# tavabE
#pyinstaller --onefile main.py
