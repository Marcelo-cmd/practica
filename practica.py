# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'examen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.Qt import QSqlDatabase
import sqlite3
from pprint import pprint



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 10, 511, 111))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(290, 110, 411, 371))
        self.tableView.setObjectName("tableView")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 180, 77, 112))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_viewdata = QtWidgets.QPushButton(self.widget)
        self.pushButton_viewdata.setObjectName("pushButton_viewdata")
        self.verticalLayout.addWidget(self.pushButton_viewdata)
        self.pushButton_addRow = QtWidgets.QPushButton(self.widget)
        self.pushButton_addRow.setObjectName("pushButton_addRow")
        self.verticalLayout.addWidget(self.pushButton_addRow)
        self.pushButton_deleteRow = QtWidgets.QPushButton(self.widget)
        self.pushButton_deleteRow.setObjectName("pushButton_deleteRow")
        self.verticalLayout.addWidget(self.pushButton_deleteRow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #----------------------AGREGACIONN DE BD----------------------

        self.create_DB()
        self.pushButton_viewdata.clicked.connect(self.print_data)
        self.model = None
        self.pushButton_viewdata.clicked.connect(self.sql_table_view_model)
        self.pushButton_addRow.clicked.connect(self.sql_add_row)
        self.pushButton_deleteRow.clicked.connect(self.sql_delete_row)
        
    def sql_delete_row(self):
        try:
            if self.model:
                self.model.removeRow(self.tableView.currentIndex().row())
            else:
                self.sql_tableview_model
        except Exception as e:
            print(e)
            
    def sql_add_row(self):
        try:
            if self.model:
                self.model.insertRows(self.model.rowCount(),1)
            else:
                self.sql_tableview_model()
        except Exception as e:
            print(e)
                 
    def sql_table_view_model(self):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('RENTALDB.db')
            
            tableview=self.tableView
            self.model= QtSql.QSqlTableModel()
            tableview.setModel(self.model)
            
            self.model.setTable('rental')
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            self.model.select()
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "rental_id")
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "rental_date")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "inventory_id")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "customer_id")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "return_date")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "staff_id")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "last_update")
        except Exception as e:
            print(e)
            
    def print_data(self):
        try:
            sqlite_file='RENTALDB.db'
            conn=sqlite3.connect(sqlite_file)
            cursor= conn.cursor()
            
            cursor.execute("SELECT * FROM 'rental' ORDER BY rental_id")
            all_rows = cursor.fetchall()
            pprint(all_rows)
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(e)
            
        
        
    def create_DB(self):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('RENTALDB.db')
            db.open() 
            
            query = QtSql.QSqlQuery() 
            
            query.exec_("create table rental(rental_id int primary key,"
                            "rental_date varchar, inventory_id int, customer varchar(20), return_date varchar(20), staff_id varchar(20), last_update varchar(20))")
            query.exec_("insert into rental values(1, '1', '21-10-2019', 'yo', '21-10-2019', '1', '21-10-2019')")
            query.exec_("insert into rental values(1, '2', '21-10-2019', 'yo', '21-10-2019', '2', '21-10-2019' )")
            query.exec_("insert into rental values(3, '3', '21-10-2019', 'yo', '21-10-2019', '3', '21-10-2019')")
            query.exec_("insert into rental values(4, '4', '21-10-2019', 'yo', '21-10-2019', '4', '21-10-2019' )")
            query.exec_("insert into rental values(5, '5', '21-10-2019', 'yo', '21-10-2019', '5', '21-10-2019' )")
        except Exception as e:
            print(e)
            
              



        #-------------------------------------------------------------

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "DATOS"))
        self.label_2.setText(_translate("MainWindow", "ACCIONES"))
        self.pushButton_viewdata.setText(_translate("MainWindow", "Ver Datos"))
        self.pushButton_addRow.setText(_translate("MainWindow", "Agregar Fila "))
        self.pushButton_deleteRow.setText(_translate("MainWindow", "Eliminar Fila "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
