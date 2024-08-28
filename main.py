from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
import sys
import MySQLdb


class MainApp(QMainWindow):

    def __init__(self):
        super(MainApp, self).__init__()

        # Load the UI file
        loadUi("library.ui", self)
        self.handle_UI_changes()
        self.handle_buttons()

    def handle_UI_changes(self):
        self.hide_themes()

    def handle_buttons(self):
        self.themes_select_button.clicked.connect(self.show_themes)
        self.ex_button.clicked.connect(self.hide_themes)

    def show_themes(self):
        self.themes_box.show()

    def hide_themes(self):
        self.themes_box.hide()


################################################################ ! ################################# TODO #################################################################
################################################################? OPEN TABS #################################################################

    def open_books_tab(self):
        pass

    def open_day_operations_tab(self):
        pass

    def open_users_tab(self):
        pass

    def open_settings_tab(self):
        pass







def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
