from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys
import requests
import webbrowser


ui, _ = loadUiType('newspider.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_buttons()

    def handel_buttons(self):
        #########################################################################################
        ###############################   External designs   ####################################

        self.pushButton.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(0, 179, 179);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 14pt \"Arial\";")

        self.pushButton_2.setStyleSheet("color: rgb(250, 255, 255);\n"
                                        "background-color: rgb(0, 179, 179);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")

        self.pushButton_3.setStyleSheet("color: rgb(250, 255, 255);\n"
                                        "background-color: rgb(0, 179, 179);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")

        self.pushButton_4.setStyleSheet("color: rgb(250, 255, 255);\n"
                                        "background-color: rgb(0, 179, 179);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")

        self.pushButton_5.setStyleSheet("color: rgb(250, 255, 255);\n"
                                        "background-color: rgb(0, 179, 179);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 10pt \"Arial\";")

        self.pushButton_6.setStyleSheet("color: rgb(250, 255, 255);\n"
                                        "background-color: rgb(0, 179, 179);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 9pt \"Arial\";")

        self.course.setStyleSheet("border-radius:12px;\n"
                                  "background-color:#f1f1f1;")

        self.book.setStyleSheet("border-radius:12px;\n"
                                "background-color:#f1f1f1;")

        ###############################   External designs   ####################################
        #########################################################################################

        self.pushButton.clicked.connect(self.course_search)
        self.pushButton_2.clicked.connect(self.movie_db)
        self.pushButton_3.clicked.connect(self.book_search)
        self.pushButton_4.clicked.connect(self.study_tab)
        self.pushButton_5.clicked.connect(self.option_tab)
        self.pushButton_6.clicked.connect(self.about_us)
        self.tabWidget.tabBar().setVisible(False)

    def course_search(self):
        course_name = self.course.text()
        if course_name:
            self.label_display_2.setText("Searching...")

            url_1 = "https://www.coursera.org/courses?query="
            response_1 = requests.get(url_1+course_name.lower())
            result_1 = str(response_1)

            url_2 = "https://www.udemy.com/courses/search/?src=ukw&q="
            response_2 = requests.get(url_2 + course_name.lower())
            result_2 = str(response_2)

            url_3 = "https://www.skillshare.com/search?query="
            response_3 = requests.get(url_3 + course_name.lower())
            result_3 = str(response_3)

            if result_2 == "<Response [200]>" or result_3 == "<Respnse [200]>":
                webbrowser.open(url_2+course_name.lower())
                webbrowser.open(url_3+course_name.lower())

                if result_1 == "<Response [200]>":
                    webbrowser.open(url_1+course_name.lower())

                    self.label_display_2.setText(
                        "Search successful of course {}.".format(course_name))
                    self.label_show.setText(
                        "Results of udemy, coursera and skillshare are opened.")
                else:
                    self.label_display_2.setText(
                        "Search successful of course {}.".format(course_name))
                    self.label_show.setText(
                        "Results of udemy and skillshare are opened.")

            else:
                self.label_display_2.setText("Invalid course input.")
                self.label_show.setText("")

        else:
            self.label_display_2.setText("Course field cannot be empty.")
            self.label_show.setText("Enter course name to search.")

    def book_search(self):
        book_name = self.book.text()

        if book_name:
            my_browser = webdriver.Chrome(
                executable_path="D:\Python\Projects\webproject\chromedriver")

            my_browser.get("https://google.com")
            my_browser.find_element_by_name(
                "q").send_keys(book_name + " doctype:pdf" + Keys.ENTER)

            self.label_display_2.setText("Showing search...")
            self.label_show.setText(
                "{} book search is visible...".format(book_name))

        else:
            self.label_display_2.setText("Book field cannot be empty.")
            self.label_show.setText("Enter book name to search.")

    def movie_db(self):
        self.label_display.setText("Searching Movie DataBase.")
        self.label_show.setText("")
        webbrowser.open("https://sanjay-xdr.github.io/Movie-Crawler/")

    def about_us(self):
        webbrowser.open(
            "https://sanjay-xdr.github.io/Movie-Crawler/about.html")

    def option_tab(self):
        self.tabWidget.setCurrentIndex(0)
        self.label_display_2.setText("")
        self.label_show.setText("")

    def study_tab(self):
        self.tabWidget.setCurrentIndex(1)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
