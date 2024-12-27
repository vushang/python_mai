import logging

logging.basicConfig(
    filename="library.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def add_copies(self, amount):
        if amount > 0:
            self.copies += amount
            logging.info(
                f"Добавлено {amount} копий книги '{self.title}'. Теперь доступно: {self.copies}"
            )
        else:
            logging.warning("Количество копий для добавления должно быть положительным.")

    def remove_copies(self, amount):
        if amount > 0:
            if self.copies >= amount:
                self.copies -= amount
                logging.info(
                    f"Удалено {amount} копий книги '{self.title}'. Осталось: {self.copies}"
                )
            else:
                logging.warning(f"Недостаточно копий книги '{self.title}' для удаления.")
        else:
            logging.warning("Количество копий для удаления должно быть положительным.")

    def get_book_info(self):
        info = f"Книга: '{self.title}', Автор: {self.author}, Копий: {self.copies}"
        logging.info(f"Запрошена информация о книге: {info}")
        return info

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        logging.info(f"Книга '{book.title}' добавлена в библиотеку.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logging.info(f"Книга '{book.title}' удалена из библиотеки.")
                return
        logging.warning(f"Книга '{title}' не найдена в библиотеке.")

    def list_books(self):
        book_list = "Список книг в библиотеке:\n"
        for book in self.books:
            book_list += f"{book.get_book_info()}\n"
        logging.info("Запрошен список всех книг в библиотеке.")
        return book_list

class Librarian:
    def __init__(self, name):
        self.name = name
        self.issued_books = []

    def issue_book(self, book, reader_name):
        if book.copies > 0:
            book.remove_copies(1)
            self.issued_books.append((book.title, reader_name))
            logging.info(
                f"Библиотекарь '{self.name}' выдал книгу '{book.title}' читателю '{reader_name}'."
            )
        else:
            logging.warning(f"Нет доступных копий книги '{book.title}' для выдачи.")

    def generate_issued_books_report(self):
        report = "Отчёт о выданных книгах:\n"
        for issue in self.issued_books:
            report += f"Книга: {issue[0]}, Читатель: {issue[1]}\n"
        logging.info(f"Сформирован отчёт о выданных книгах библиотекаря '{self.name}'.")
        return report

book1 = Book("1984", "Джордж Оруэлл", 5)
book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 3)

library = Library()
library.add_book(book1)
library.add_book(book2)

librarian = Librarian("Анна Иванова")
librarian.issue_book(book1, "Иван Сидоров")
librarian.issue_book(book2, "Мария Петрова")

print(librarian.generate_issued_books_report())
print(library.list_books())