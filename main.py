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
        self.add_new_book_btn.clicked.connect(self.add_new_books)
        self.add_new_cat_btn.clicked.connect(self.add_category)

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
        self.db = MySQLdb.connect(
            host="localhost", user="root", password="ASDfgh2580.", database="library"
        )
        self.cur = self.db.cursor()

        book_title = self.add_book_line.text()
        book_code = self.book_code_line.text()
        book_category = self.book_category_box.CurrentText()
        book_author = self.add_author_box.CurrentText()
        book_publisher = self.add_publisher_box.CurrentText()
        book_price = self.add_book_price.text()

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

    ################################################################TODO SETTİNGS SET #################################################################

    def add_category(self):
        self.db = MySQLdb.connect(
            host="localhost", user="root", password="ASDfgh2580.", database="library"
        )
        self.cur = self.db.cursor()

        category_name = self.new_category_line.text()
        self.cur.execute(
            """INSERT INTO category (category_name) VALUES (%s) """, (category_name,)
        )

        self.db.commit()
        self.statusBar().showMessage('New category Added!')

    def add_author(self):
        self.db = MySQLdb.connect(
            host="localhost", user="root", password="ASDfgh2580.", database="library"
        )
        self.cur = self.db.cursor()

        author_name = self.new_author_line.text()
        self.cur.execute(
            """INSERT INTO authors (author_name) VALUES (%s) """, (author_name,)
        )

        self.db.commit()
        self.statusBar().showMessage('New Author Added!')

    def app_publisher(self):
        self.db = MySQLdb.connect(
            host="localhost", user="root", password="ASDfgh2580.", database="library"
        )
        self.cur = self.db.cursor()

        publisher_name = self.new_publisher_line.text()
        self.cur.execute(
            """INSERT INTO publisher (publisher_name) VALUES (%s) """, (publisher_name,)
        )

        self.db.commit()
        self.statusBar().showMessage('New Publisher Added!')


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
