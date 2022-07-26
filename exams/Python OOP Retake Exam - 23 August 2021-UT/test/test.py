import unittest

from project.library import Library
# from library import Library


class LibraryTest(unittest.TestCase):
    name = 'Name'
    invalid_name = ''

    def setUp(self) -> None:
        self.library = Library(self.name)

    def test_init(self):
        self.assertEqual(self.name, self.library.name)
        self.assertDictEqual({}, self.library.books_by_authors)
        self.assertDictEqual({}, self.library.readers)

    def test_name_raise(self):
        with self.assertRaises(ValueError) as err:
            self.library.name = self.invalid_name

        self.assertEqual('Name cannot be empty string!', str(err.exception))

    def test_name_correct(self):
        new_name = 'new'
        self.library.name = new_name
        self.assertEqual(new_name, self.library.name)

    def test_add_book_without_author(self):
        new_author = "new_author"
        new_title = 'new_title'
        self.library.add_book(new_author, new_title)
        self.assertDictEqual(self.library.books_by_authors, {new_author: [new_title]})

    def test_add_book_without_title(self):
        new_author = "new_author"
        new_title = 'new_title'
        sec_new_title = 'sec_new_title'
        self.library.add_book(new_author, new_title)
        self.library.add_book(new_author, sec_new_title)
        self.assertDictEqual(self.library.books_by_authors, {new_author: [new_title, sec_new_title]})

    def test_add_reader_successfully_added(self):
        new_reader = 'new_reader'
        self.library.add_reader(new_reader)
        self.assertDictEqual(self.library.readers, {new_reader: []})

    def test_add_reader_already_added(self):
        new_reader = 'new_reader'
        self.library.add_reader(new_reader)
        result = self.library.add_reader(new_reader)
        self.assertEqual(result, f"{new_reader} is already registered in the {self.library.name} library.")

    def test_rent_book_if_reader_not_in_library(self):
        new_reader = 'new_reader'
        new_author = "new_author"
        new_title = 'new_title'
        sec_new_title = 'sec_new_title'
        result = self.library.rent_book(new_reader, new_author, new_title)
        self.assertEqual(f"{new_reader} is not registered in the {self.library.name} Library.", result)

    def test_rent_book_if_author_not_in_library(self):
        new_reader = 'new_reader'
        new_author = "new_author"
        new_title = 'new_title'
        sec_new_title = 'sec_new_title'
        self.library.add_reader(new_reader)
        result = self.library.rent_book(new_reader, new_author, new_title)
        self.assertEqual(f"{self.library.name} Library does not have any {new_author}'s books.", result)

    def test_rent_book_if_title_not_in_library(self):
        new_reader = 'new_reader'
        new_author = "new_author"
        new_title = 'new_title'
        sec_new_title = 'sec_new_title'
        self.library.add_reader(new_reader)
        self.library.add_book(new_author, new_title)
        result = self.library.rent_book(new_reader, new_author, sec_new_title)
        self.assertEqual(f"""{self.library.name} Library does not have {new_author}'s "{sec_new_title}".""", result)

    def test_rent_book_if_all_in_library(self):
        new_reader = 'new_reader'
        new_author = "new_author"
        new_title = 'new_title'
        sec_new_title = 'sec_new_title'
        self.library.add_reader(new_reader)
        self.library.add_book(new_author, new_title)
        self.library.rent_book(new_reader, new_author, new_title)
        result = self.library.readers
        self.assertEqual({new_reader: [{new_author: new_title}]}, result)
        self.assertEqual(True, new_title not in self.library.books_by_authors)
        self.assertEqual(self.library.books_by_authors, {'new_author': []})


