import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtCore import Slot, QFile, QTextStream

from sidebar import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.content_stackedWidget.setCurrentIndex(0)
        self.ui.home_btn.setChecked(True)

    ## Function for searching
    @Slot()
    def on_search_btn_clicked(self):
        print(5555)
        self.ui.content_stackedWidget.setCurrentWidget(self.ui.page_search)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_search.setText(search_text)

    ## Function for changing page to user page
    @Slot()
    def on_user_btn_clicked(self):
        self.ui.content_stackedWidget.setCurrentIndex(3)

    ## Change QPushButton Checkable status when stackedWidget index changed
    @Slot()
    def on_content_stackedWidget_currentChanged(self):
        btn_list = self.ui.sidebar_items_box_widget.findChildren(QPushButton)
        for btn in btn_list:
            btn.setAutoExclusive(True)
            
    ## functions for changing sidebar page
    @Slot()
    def on_home_btn_clicked(self):
        self.ui.content_stackedWidget.setCurrentIndex(0)

    @Slot()
    def on_dashborad_btn_clicked(self):
        self.ui.content_stackedWidget.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ## loading style file
    # with open("style.qss", "r") as style_file:
    #     style_str = style_file.read()
    # app.setStyleSheet(style_str)

    ## loading style file, Example 2
    style_file = QFile("style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())


    window = MainWindow()
    window.show()

    sys.exit(app.exec())



