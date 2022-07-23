from project.bookstore import Bookstore
from unittest import TestCase


class BookstoreTest(TestCase):
    BOOK_LIMIT = 1

    def setUp(self) -> None:
        self.bookstore = Bookstore(self.BOOK_LIMIT)

    def test_init_raise_when_limit_is_zero(self):
        with self.assertRaises(ValueError) as err:
            self.bookstore.books_limit = self.BOOK_LIMIT - 1
        self.assertEqual(str(err.exception), f"Books limit of {self.BOOK_LIMIT - 1} is not valid")
        self.assertEqual(self.BOOK_LIMIT, self.bookstore.books_limit)

    def test_init_raise_when_limit_is_negative(self):
        with self.assertRaises(ValueError) as err:
            self.bookstore.books_limit = self.BOOK_LIMIT - 2
        self.assertEqual(str(err.exception), f"Books limit of {self.BOOK_LIMIT - 2} is not valid")
        self.assertEqual(self.BOOK_LIMIT, self.bookstore.books_limit)

    def test_init_correct(self):
        self.assertEqual(self.BOOK_LIMIT, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)

    def test_len(self):
        self.bookstore.books_limit = self.BOOK_LIMIT + 10
        result1 = len(self.bookstore)
        self.assertEqual(0, result1)
        self.bookstore.receive_book('Book', 1)
        self.bookstore.receive_book('Book2', 2)
        result2 = len(self.bookstore)
        self.assertEqual(3, result2)

    def test_receive_book_if_no_space_raise(self):
        with self.assertRaises(Exception) as err:
            self.bookstore.receive_book('Book2', 2)
        self.assertEqual(str(err.exception), "Books limit is reached. Cannot receive more books!")
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)

    def test_receive_book_if_one_space_raise(self):
        self.bookstore.receive_book('Book2', 1)
        with self.assertRaises(Exception) as err:
            self.bookstore.receive_book('Book2', 1)
        self.assertEqual(str(err.exception), "Books limit is reached. Cannot receive more books!")
        self.assertEqual({'Book2': 1}, self.bookstore.availability_in_store_by_book_titles)

    def test_receive_book_if_enough_space(self):
        self.bookstore.books_limit = self.BOOK_LIMIT + 10
        self.bookstore.receive_book('Book', 1)
        self.bookstore.receive_book('Book2', 2)
        result2 = len(self.bookstore)
        self.assertEqual(3, result2)

    def test_receive_book_if_enough_space_return(self):
        self.bookstore.books_limit = self.BOOK_LIMIT + 10
        book_name = "Book2"
        book_count = 2
        result = self.bookstore.receive_book(book_name, book_count)
        self.assertEqual(f"{book_count} copies of {book_name} are available in the bookstore.", result)

    def test_sell_book_if_not_there_raise(self):
        self.bookstore.books_limit = self.BOOK_LIMIT + 10
        book_name = "Book2"
        second_book_name = 'Book'
        book_count = 2
        second_book_count = 1
        self.bookstore.receive_book(book_name, book_count)
        with self.assertRaises(Exception) as err:
            self.bookstore.sell_book(second_book_name, second_book_count)
        self.assertEqual(str(err.exception), f"Book {second_book_name} doesn't exist!")
        self.assertEqual({book_name: book_count}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_if_not_numbers_raise(self):
        self.bookstore.books_limit = self.BOOK_LIMIT + 10
        book_name = "Book2"

        book_count = 2

        self.bookstore.receive_book(book_name, book_count)
        with self.assertRaises(Exception) as err:
            self.bookstore.sell_book(book_name, book_count + 1)
        self.assertEqual(str(err.exception), f"{book_name} has not enough copies to sell. Left: {book_count}")

        self.assertEqual({book_name: book_count}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_correct(self):
        self.bookstore.books_limit = self.BOOK_LIMIT + 10
        book_name = "Book2"
        book_count = 2
        self.bookstore.receive_book(book_name, book_count)
        result = self.bookstore.sell_book(book_name, book_count - 1)
        self.assertEqual(result, f"Sold {book_count - 1} copies of {book_name}")

        self.assertEqual({book_name: book_count - 1}, self.bookstore.availability_in_store_by_book_titles)

    def test_str(self):
        self.bookstore.books_limit = self.BOOK_LIMIT + 10
        book_name = "Book2"
        second_book_name = 'Book'
        book_count = 2
        second_book_count = 1
        self.bookstore.receive_book(book_name, book_count)
        self.bookstore.sell_book(book_name, book_count - 1)
        self.bookstore.receive_book(second_book_name, second_book_count)
        expected = f"Total sold books: {book_count - 1}" + \
                   '\n' + f'Current availability: {len(self.bookstore)}' + \
                   '\n' + f" - {book_name}: {book_count - 1} copies" + \
                   '\n' + f" - {second_book_name}: {second_book_count} copies"
        actual = str(self.bookstore)
        self.assertEqual(actual, expected)

    def test_str_no_books(self):
        self.bookstore.books_limit = self.BOOK_LIMIT + 10

        expected = f"Total sold books: 0" + \
                   '\n' + f'Current availability: 0'
        actual = str(self.bookstore)
        self.assertEqual(actual, expected)

