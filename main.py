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
        self.day_tab.tabBar().setVisible(False)
        #! btn activate the project menu

    def handle_buttons(self):
        self.themes_select_button.clicked.connect(self.show_themes)
        self.ex_button.clicked.connect(self.hide_themes)
        self.date_btn.clicked.connect(self.open_day_operations_tab)
        self.book_btn.clicked.connect(self.open_books_tab)
        self.user_btn.clicked.connect(self.open_users_tab)
        self.setting_btn.clicked.connect(self.open_settings_tab)

    def show_themes(self):
        self.themes_box.show()

    def hide_themes(self):
        self.themes_box.hide()

    ################################################################ ! ################################# TODO #################################################################
    ################################################################? OPEN TABS #################################################################

    def open_day_operations_tab(self):
        self.day_tab.setCurrentIndex(0)

    def open_books_tab(self):
        self.day_tab.setCurrentIndex(1)

    def open_users_tab(self):
        self.day_tab.setCurrentIndex(2)

    def open_settings_tab(self):
        self.day_tab.setCurrentIndex(3)

    ################################################################TODO BOOKS SET #################################################################
    def add_new_books(self):
        pass

    def search_books(self):
        pass

    def edit_books(self):
        pass

    def delete_books(self):
        pass

    ################################################################TODO USERS SET #################################################################

    def add_new_user(self):
        pass

    def Login(self):
        pass

    def edit_user(self):
        pass
    


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
