# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Thu Apr  3 21:29:48 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 821)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayoutMainWindow = QtGui.QGridLayout()
        self.gridLayoutMainWindow.setObjectName("gridLayoutMainWindow")
        self.pushButtonSubSectionAdd = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSubSectionAdd.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonSubSectionAdd.setObjectName("pushButtonSubSectionAdd")
        self.gridLayoutMainWindow.addWidget(self.pushButtonSubSectionAdd, 4, 1, 1, 1)
        self.listWidgetSection = QtGui.QListWidget(self.centralwidget)
        self.listWidgetSection.setMaximumSize(QtCore.QSize(16777215, 130))
        self.listWidgetSection.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        self.listWidgetSection.setAlternatingRowColors(False)
        self.listWidgetSection.setMovement(QtGui.QListView.Free)
        self.listWidgetSection.setSelectionRectVisible(True)
        self.listWidgetSection.setObjectName("listWidgetSection")
        QtGui.QListWidgetItem(self.listWidgetSection)
        QtGui.QListWidgetItem(self.listWidgetSection)
        QtGui.QListWidgetItem(self.listWidgetSection)
        QtGui.QListWidgetItem(self.listWidgetSection)
        QtGui.QListWidgetItem(self.listWidgetSection)
        QtGui.QListWidgetItem(self.listWidgetSection)
        self.gridLayoutMainWindow.addWidget(self.listWidgetSection, 2, 0, 1, 4)
        self.labelSentence = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelSentence.setFont(font)
        self.labelSentence.setObjectName("labelSentence")
        self.gridLayoutMainWindow.addWidget(self.labelSentence, 0, 4, 1, 1)
        self.labelSubSection = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelSubSection.setFont(font)
        self.labelSubSection.setObjectName("labelSubSection")
        self.gridLayoutMainWindow.addWidget(self.labelSubSection, 3, 0, 1, 4)
        self.labelHowTo = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelHowTo.setFont(font)
        self.labelHowTo.setObjectName("labelHowTo")
        self.gridLayoutMainWindow.addWidget(self.labelHowTo, 6, 0, 1, 4)
        self.lineEditSection = QtGui.QLineEdit(self.centralwidget)
        self.lineEditSection.setText("")
        self.lineEditSection.setObjectName("lineEditSection")
        self.gridLayoutMainWindow.addWidget(self.lineEditSection, 1, 0, 1, 1)
        self.lineEditSubSection = QtGui.QLineEdit(self.centralwidget)
        self.lineEditSubSection.setObjectName("lineEditSubSection")
        self.gridLayoutMainWindow.addWidget(self.lineEditSubSection, 4, 0, 1, 1)
        self.lineEditHowTo = QtGui.QLineEdit(self.centralwidget)
        self.lineEditHowTo.setObjectName("lineEditHowTo")
        self.gridLayoutMainWindow.addWidget(self.lineEditHowTo, 7, 0, 1, 1)
        self.labelSection = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelSection.setFont(font)
        self.labelSection.setObjectName("labelSection")
        self.gridLayoutMainWindow.addWidget(self.labelSection, 0, 0, 1, 1)
        self.pushButtonAddSection = QtGui.QPushButton(self.centralwidget)
        self.pushButtonAddSection.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonAddSection.setObjectName("pushButtonAddSection")
        self.gridLayoutMainWindow.addWidget(self.pushButtonAddSection, 1, 1, 1, 1)
        self.listWidgetHowTo = QtGui.QListWidget(self.centralwidget)
        self.listWidgetHowTo.setMidLineWidth(0)
        self.listWidgetHowTo.setAlternatingRowColors(False)
        self.listWidgetHowTo.setMovement(QtGui.QListView.Free)
        self.listWidgetHowTo.setSelectionRectVisible(True)
        self.listWidgetHowTo.setObjectName("listWidgetHowTo")
        QtGui.QListWidgetItem(self.listWidgetHowTo)
        QtGui.QListWidgetItem(self.listWidgetHowTo)
        self.gridLayoutMainWindow.addWidget(self.listWidgetHowTo, 8, 0, 1, 4)
        self.pushButtonAddSentence = QtGui.QPushButton(self.centralwidget)
        self.pushButtonAddSentence.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonAddSentence.setObjectName("pushButtonAddSentence")
        self.gridLayoutMainWindow.addWidget(self.pushButtonAddSentence, 0, 5, 1, 1)
        self.pushButtonHotToAdd = QtGui.QPushButton(self.centralwidget)
        self.pushButtonHotToAdd.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonHotToAdd.setObjectName("pushButtonHotToAdd")
        self.gridLayoutMainWindow.addWidget(self.pushButtonHotToAdd, 7, 1, 1, 1)
        self.pushButtonRemove = QtGui.QPushButton(self.centralwidget)
        self.pushButtonRemove.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.gridLayoutMainWindow.addWidget(self.pushButtonRemove, 1, 2, 1, 1)
        self.tableWidgetSentence = QtGui.QTableWidget(self.centralwidget)
        self.tableWidgetSentence.setAlternatingRowColors(True)
        self.tableWidgetSentence.setObjectName("tableWidgetSentence")
        self.tableWidgetSentence.setColumnCount(1)
        self.tableWidgetSentence.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSentence.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSentence.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSentence.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSentence.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSentence.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSentence.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSentence.setItem(2, 0, item)
        self.tableWidgetSentence.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidgetSentence.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetSentence.verticalHeader().setStretchLastSection(False)
        self.gridLayoutMainWindow.addWidget(self.tableWidgetSentence, 3, 4, 6, 4)
        self.pushButtonHowToUpdate = QtGui.QPushButton(self.centralwidget)
        self.pushButtonHowToUpdate.setObjectName("pushButtonHowToUpdate")
        self.gridLayoutMainWindow.addWidget(self.pushButtonHowToUpdate, 7, 3, 1, 1)
        self.listWidgetSebSection = QtGui.QListWidget(self.centralwidget)
        self.listWidgetSebSection.setMaximumSize(QtCore.QSize(16777215, 150))
        self.listWidgetSebSection.setAlternatingRowColors(False)
        self.listWidgetSebSection.setMovement(QtGui.QListView.Free)
        self.listWidgetSebSection.setSelectionRectVisible(True)
        self.listWidgetSebSection.setObjectName("listWidgetSebSection")
        QtGui.QListWidgetItem(self.listWidgetSebSection)
        QtGui.QListWidgetItem(self.listWidgetSebSection)
        QtGui.QListWidgetItem(self.listWidgetSebSection)
        QtGui.QListWidgetItem(self.listWidgetSebSection)
        QtGui.QListWidgetItem(self.listWidgetSebSection)
        QtGui.QListWidgetItem(self.listWidgetSebSection)
        self.gridLayoutMainWindow.addWidget(self.listWidgetSebSection, 5, 0, 1, 4)
        self.pushButtonSectionUpdate = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSectionUpdate.setObjectName("pushButtonSectionUpdate")
        self.gridLayoutMainWindow.addWidget(self.pushButtonSectionUpdate, 1, 3, 1, 1)
        self.pushButtonSubSectionRemove = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSubSectionRemove.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonSubSectionRemove.setObjectName("pushButtonSubSectionRemove")
        self.gridLayoutMainWindow.addWidget(self.pushButtonSubSectionRemove, 4, 2, 1, 1)
        self.pushButtonHowToRemove = QtGui.QPushButton(self.centralwidget)
        self.pushButtonHowToRemove.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonHowToRemove.setObjectName("pushButtonHowToRemove")
        self.gridLayoutMainWindow.addWidget(self.pushButtonHowToRemove, 7, 2, 1, 1)
        self.pushButtonSubSectionUpdate = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSubSectionUpdate.setObjectName("pushButtonSubSectionUpdate")
        self.gridLayoutMainWindow.addWidget(self.pushButtonSubSectionUpdate, 4, 3, 1, 1)
        self.pushButtonUpdateSentence = QtGui.QPushButton(self.centralwidget)
        self.pushButtonUpdateSentence.setMaximumSize(QtCore.QSize(85, 16777215))
        self.pushButtonUpdateSentence.setObjectName("pushButtonUpdateSentence")
        self.gridLayoutMainWindow.addWidget(self.pushButtonUpdateSentence, 0, 7, 1, 1)
        self.pushButtonRemoveSentence = QtGui.QPushButton(self.centralwidget)
        self.pushButtonRemoveSentence.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonRemoveSentence.setObjectName("pushButtonRemoveSentence")
        self.gridLayoutMainWindow.addWidget(self.pushButtonRemoveSentence, 0, 6, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(500, 0))
        self.textEdit.setObjectName("textEdit")
        self.gridLayoutMainWindow.addWidget(self.textEdit, 1, 4, 2, 4)
        self.gridLayout_2.addLayout(self.gridLayoutMainWindow, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 990, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSection = QtGui.QMenu(self.menubar)
        self.menuSection.setObjectName("menuSection")
        self.menuSubSection = QtGui.QMenu(self.menubar)
        self.menuSubSection.setObjectName("menuSubSection")
        self.menuHowTo = QtGui.QMenu(self.menubar)
        self.menuHowTo.setObjectName("menuHowTo")
        self.menuSentence = QtGui.QMenu(self.menubar)
        self.menuSentence.setObjectName("menuSentence")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtGui.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionPrint = QtGui.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionTips = QtGui.QAction(MainWindow)
        self.actionTips.setObjectName("actionTips")
        self.actionAddSection = QtGui.QAction(MainWindow)
        self.actionAddSection.setObjectName("actionAddSection")
        self.actionRemoveSection = QtGui.QAction(MainWindow)
        self.actionRemoveSection.setObjectName("actionRemoveSection")
        self.actionUpdateSection = QtGui.QAction(MainWindow)
        self.actionUpdateSection.setObjectName("actionUpdateSection")
        self.actionAddSubSection = QtGui.QAction(MainWindow)
        self.actionAddSubSection.setObjectName("actionAddSubSection")
        self.actionRemoveSubSection = QtGui.QAction(MainWindow)
        self.actionRemoveSubSection.setObjectName("actionRemoveSubSection")
        self.actionUpdateSubSection = QtGui.QAction(MainWindow)
        self.actionUpdateSubSection.setObjectName("actionUpdateSubSection")
        self.actionAddHowTo = QtGui.QAction(MainWindow)
        self.actionAddHowTo.setObjectName("actionAddHowTo")
        self.actionRemoveHowTo = QtGui.QAction(MainWindow)
        self.actionRemoveHowTo.setObjectName("actionRemoveHowTo")
        self.actionUpdateHowTo = QtGui.QAction(MainWindow)
        self.actionUpdateHowTo.setObjectName("actionUpdateHowTo")
        self.actionAddSentence = QtGui.QAction(MainWindow)
        self.actionAddSentence.setObjectName("actionAddSentence")
        self.actionRemoveSentence = QtGui.QAction(MainWindow)
        self.actionRemoveSentence.setObjectName("actionRemoveSentence")
        self.actionUpdateSentence = QtGui.QAction(MainWindow)
        self.actionUpdateSentence.setObjectName("actionUpdateSentence")
        self.actionImportXML = QtGui.QAction(MainWindow)
        self.actionImportXML.setObjectName("actionImportXML")
        self.actionExportXML = QtGui.QAction(MainWindow)
        self.actionExportXML.setObjectName("actionExportXML")
        self.actionImportJSON = QtGui.QAction(MainWindow)
        self.actionImportJSON.setObjectName("actionImportJSON")
        self.actionExportJSON = QtGui.QAction(MainWindow)
        self.actionExportJSON.setObjectName("actionExportJSON")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImportXML)
        self.menuFile.addAction(self.actionExportXML)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImportJSON)
        self.menuFile.addAction(self.actionExportJSON)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionTips)
        self.menuHelp.addAction(self.actionAbout)
        self.menuSection.addAction(self.actionAddSection)
        self.menuSection.addAction(self.actionRemoveSection)
        self.menuSection.addAction(self.actionUpdateSection)
        self.menuSubSection.addAction(self.actionAddSubSection)
        self.menuSubSection.addAction(self.actionRemoveSubSection)
        self.menuSubSection.addAction(self.actionUpdateSubSection)
        self.menuHowTo.addAction(self.actionAddHowTo)
        self.menuHowTo.addAction(self.actionRemoveHowTo)
        self.menuHowTo.addAction(self.actionUpdateHowTo)
        self.menuSentence.addAction(self.actionAddSentence)
        self.menuSentence.addAction(self.actionRemoveSentence)
        self.menuSentence.addAction(self.actionUpdateSentence)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSection.menuAction())
        self.menubar.addAction(self.menuSubSection.menuAction())
        self.menubar.addAction(self.menuHowTo.menuAction())
        self.menubar.addAction(self.menuSentence.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Sci Corpus ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSubSectionAdd.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidgetSection.isSortingEnabled()
        self.listWidgetSection.setSortingEnabled(False)
        self.listWidgetSection.item(0).setText(QtGui.QApplication.translate("MainWindow", "Abstract", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetSection.item(1).setText(QtGui.QApplication.translate("MainWindow", "Introduction", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetSection.item(2).setText(QtGui.QApplication.translate("MainWindow", "Methodology", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetSection.item(3).setText(QtGui.QApplication.translate("MainWindow", "Results", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetSection.item(4).setText(QtGui.QApplication.translate("MainWindow", "Discussion", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetSection.item(5).setText(QtGui.QApplication.translate("MainWindow", "Conclusion", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetSection.setSortingEnabled(__sortingEnabled)
        self.labelSentence.setText(QtGui.QApplication.translate("MainWindow", "Sentece", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSubSection.setText(QtGui.QApplication.translate("MainWindow", " Sub Section", None, QtGui.QApplication.UnicodeUTF8))
        self.labelHowTo.setText(QtGui.QApplication.translate("MainWindow", "How To", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSection.setText(QtGui.QApplication.translate("MainWindow", " Section", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddSection.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidgetHowTo.isSortingEnabled()
        self.listWidgetHowTo.setSortingEnabled(False)
        self.listWidgetHowTo.item(0).setText(QtGui.QApplication.translate("MainWindow", "Cite previous research", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetHowTo.item(1).setText(QtGui.QApplication.translate("MainWindow", "Present a hipotesys", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetHowTo.setSortingEnabled(__sortingEnabled)
        self.pushButtonAddSentence.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonHotToAdd.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRemove.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetSentence.setSortingEnabled(True)
        self.tableWidgetSentence.verticalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetSentence.verticalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetSentence.verticalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetSentence.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Sentence", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tableWidgetSentence.isSortingEnabled()
        self.tableWidgetSentence.setSortingEnabled(False)
        self.tableWidgetSentence.item(0, 0).setText(QtGui.QApplication.translate("MainWindow", "a teste", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetSentence.item(1, 0).setText(QtGui.QApplication.translate("MainWindow", "b teste", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetSentence.item(2, 0).setText(QtGui.QApplication.translate("MainWindow", "c teste", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetSentence.setSortingEnabled(__sortingEnabled)
        self.pushButtonHowToUpdate.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidgetSebSection.isSortingEnabled()
        self.listWidgetSebSection.setSortingEnabled(False)
        self.listWidgetSebSection.item(0).setText(QtGui.QApplication.translate("MainWindow", "Context", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetSebSection.item(1).setText(QtGui.QApplication.translate("MainWindow", "Gap", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetSebSection.item(2).setText(QtGui.QApplication.translate("MainWindow", "Propose", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetSebSection.item(3).setText(QtGui.QApplication.translate("MainWindow", "Methodology", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetSebSection.item(4).setText(QtGui.QApplication.translate("MainWindow", "Result", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetSebSection.item(5).setText(QtGui.QApplication.translate("MainWindow", "Conclusion", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetSebSection.setSortingEnabled(__sortingEnabled)
        self.pushButtonSectionUpdate.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSubSectionRemove.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonHowToRemove.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSubSectionUpdate.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonUpdateSentence.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRemoveSentence.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Type here your sentence and press enter to add.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSection.setTitle(QtGui.QApplication.translate("MainWindow", "Section", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSubSection.setTitle(QtGui.QApplication.translate("MainWindow", "Sub Section", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHowTo.setTitle(QtGui.QApplication.translate("MainWindow", "How To", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSentence.setTitle(QtGui.QApplication.translate("MainWindow", "Sentence", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setText(QtGui.QApplication.translate("MainWindow", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTips.setText(QtGui.QApplication.translate("MainWindow", "Tips", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddSection.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveSection.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateSection.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddSubSection.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveSubSection.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateSubSection.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddHowTo.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveHowTo.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateHowTo.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddSentence.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveSentence.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateSentence.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportXML.setText(QtGui.QApplication.translate("MainWindow", "Import XML", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportXML.setText(QtGui.QApplication.translate("MainWindow", "Export XML", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportJSON.setText(QtGui.QApplication.translate("MainWindow", "Import JSON", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportJSON.setText(QtGui.QApplication.translate("MainWindow", "Export JSON", None, QtGui.QApplication.UnicodeUTF8))

