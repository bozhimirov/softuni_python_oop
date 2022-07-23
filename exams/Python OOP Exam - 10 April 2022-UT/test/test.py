from project.movie import Movie

from unittest import TestCase

# from movie import Movie


class MovieTest(TestCase):
    NAME = 'NAME'
    YEAR = 1887
    RATING = 5.5

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test_init(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_if_empty_string_raise(self):
        with self.assertRaises(ValueError) as err:
            self.movie.name = ''
        self.assertEqual(str(err.exception), "Name cannot be an empty string!")
        self.assertEqual(self.NAME, self.movie.name)

    def test_year_lt_raise(self):
        with self.assertRaises(ValueError) as err:
            self.movie.year = self.YEAR - 1
        self.assertEqual(str(err.exception), "Year is not valid!")
        self.assertEqual(self.YEAR, self.movie.year)

    def test_add_actor_if_there_raise(self):
        actor_name = 'actor'
        self.movie.add_actor(actor_name)
        result = self.movie.add_actor(actor_name)
        self.assertEqual(result, f"{actor_name} is already added in the list of actors!")
        self.assertEqual([actor_name], self.movie.actors)

    def test_add_actor_if_not_there(self):
        actor_name = 'actor'
        self.movie.add_actor(actor_name)
        self.assertEqual([actor_name], self.movie.actors)

    def test_gt_if_one_self_is_better(self):
        movie2_rating = 5.1
        self.movie2 = Movie('movie2', 1900, movie2_rating)
        result = self.movie.__gt__(self.movie2)
        self.assertEqual(result, f'"{self.movie.name}" is better than "{self.movie2.name}"')

    def test_gt_if_other_is_better(self):
        movie2_rating = 5.1
        self.movie2 = Movie('movie2', 1900, movie2_rating)
        result = self.movie2.__gt__(self.movie)
        self.assertEqual(result, f'"{self.movie.name}" is better than "{self.movie2.name}"')

    def test_repr(self):
        actor1 = 'actor1'
        actor2 = 'actor2'
        self.movie.add_actor(actor1)
        self.movie.add_actor(actor2)
        expected = f"Name: {self.NAME}\n" \
                   f"Year of Release: {self.YEAR}\n" \
                   f"Rating: {self.RATING:.2f}\n" \
                   f"Cast: {actor1}, {actor2}"
        actual = repr(self.movie)
        self.assertEqual(expected, actual)

