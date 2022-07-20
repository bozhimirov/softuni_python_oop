import unittest


class IntegerListTest(unittest.TestCase):

    def test_is_initialize_correctly_without_data(self):
        integer = IntegerList()
        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialize_correctly_withwrong_data(self):
        integer = IntegerList('asd', 5.4, 5.55)
        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialize_correctly_with_int_data(self):
        integer = IntegerList('asd', 5)
        self.assertEqual([5], integer._IntegerList__data)

    def test_get_data(self):
        integer = IntegerList(5, 'asd')
        self.assertEqual([5], integer._IntegerList__data)

        result = integer.get_data()
        self.assertEqual([5], result)

    def test_add_method_incorrect_data_raises(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)

        with self.assertRaises(ValueError) as ex:
            integer.add('5')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_add_method_correct_data(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)

        integer.add(10)
        self.assertEqual([5, 10], integer._IntegerList__data)

    def test_removes_el_removes_the_element(self):
        integer = IntegerList(5)
        integer.remove_index(0)
        self.assertEqual([], integer._IntegerList__data)
        # self.assertEqual(0, len(integer._IntegerLlist__data))

    def test_remove_invalid_index_raises(self):
        integer = IntegerList(5)
        with self.assertRaises(IndexError) as ex:
            integer.remove_index(1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_returns_element_at_the_removed_index(self):
        integer = IntegerList(5)
        result = integer.remove_index(0)
        self.assertEqual(5, result)

    def test_get_with_invalid_index_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.get(2)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            integer.get(1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_valid_index_return_element(self):
        integer = IntegerList(5)

        result = integer.get(0)

        self.assertEqual(5, result)

    def test_insert_invalid_index_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.insert(2, 10)

        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert_invalid_data_type_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(ValueError) as ex:
            integer.insert(0, "10")

        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_insert_adds_element(self):
        integer = IntegerList(5)

        integer.insert(0, 10)
        self.assertEqual([10, 5], integer._IntegerList__data)

    def test_get_biggest(self):
        integer = IntegerList(5, -2, 0, 100, 6, -456, 90)
        result = integer.get_biggest()
        self.assertEqual(100, result)

    def test_get_index(self):
        integer = IntegerList(5, -2, 0, 100, 6, -456, 90)
        result = integer.get_index(-2)
        self.assertEqual(1, result)

        result = integer.get_index(6)
        self.assertEqual(4, result)


if __name__ == "__main__":
    unittest.main()
