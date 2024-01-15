BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}(id_={self.id}, '
                f'name={self.name!r}, pages={self.pages})')


class Library:
    def __init__(self, books: list[Book] = None):
        if books is not None:
            if not isinstance(books, list):
                raise TypeError("атрибут books должен быть типа list")
            for book in books:
                if not isinstance(book, Book):
                    raise TypeError("элементы books должны быть типа Book")
        self.books = books if books is not None else []

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            return max(self.books, key=lambda x: x.id).id + 1

    def get_index_by_book_id(self, id_):
        for i, book in enumerate(self.books):
            if book.id == id_:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
