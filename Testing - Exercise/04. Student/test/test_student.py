import unittest

from project.student import Student


class StudentTest(unittest.TestCase):
    STUDENT_NAME = 'One'

    def setUp(self) -> None:
        self.student = Student(self.STUDENT_NAME)

    def test_student_init_without_courses(self):
        self.assertEqual(self.STUDENT_NAME, self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_student_init_with_courses(self):
        course = {'Python': ['note1', 'note2']}

        student = Student(self.STUDENT_NAME, course)

        self.assertEqual(self.STUDENT_NAME, student.name)
        self.assertEqual(course, student.courses)

    def test_enroll_student_updates_course_notes_when_already(self):
        course_name = 'Python OOP'
        courses = {course_name: ["note 1", "note 2"]}

        student = Student(self.STUDENT_NAME, courses)

        result = student.enroll(course_name, ['note 3', 'note 4'])

        self.assertEqual('Course already added. Notes have been updated.', result)
        self.assertEqual(['note 1', 'note 2', 'note 3', 'note 4'], student.courses[course_name])

    def test_enroll_student_extend_course_when_no_notes(self):
        course_name = 'Python Adv'
        course_notes = ["note 1", "note 2"]

        result = self.student.enroll(course_name, course_notes)

        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual(course_notes, self.student.courses[course_name])

    def test_enroll_student_extend_course_when_notes_y(self):
        course_name = 'Python Adv'
        course_notes = ["note 1", "note 2"]

        result = self.student.enroll(course_name, course_notes, 'Y')

        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual(course_notes, self.student.courses[course_name])

    def test_enroll_student_extend_course_with_wrong_argument(self):
        course_name = 'Python Adv'
        course_notes = ["note 1", "note 2"]

        result = self.student.enroll(course_name, course_notes, 'N')

        self.assertEqual('Course has been added.', result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual([], self.student.courses[course_name])

    def test_add_notes_raises_err_when_course_not_exists(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Python Advanced', 'Note 8')
        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_add_notes_updates_course_notes_when_course_exists(self):
        course_name = 'Python OOP'
        courses = {course_name: ["note 1", "note 2"]}

        student = Student(self.STUDENT_NAME, courses)

        result = student.add_notes(course_name, 'note 3')

        self.assertEqual('Notes have been updated', result)
        self.assertEqual(['note 1', 'note 2', 'note 3'], student.courses[course_name])

    def test_leave_course_rises_err_when_course_not_exists(self):
        self.student.enroll('P Basics', [])

        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Python OOP')
        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))

    def test_leave_course_removes_course_when_student_is_enrolled_for_course(self):
        course_name = 'Python Advanced'
        student = Student(self.STUDENT_NAME, {course_name: []})

        result = student.leave_course(course_name)

        self.assertEqual('Course has been removed', result)
        self.assertTrue(course_name not in student.courses)


if __name__ == '__main__':
    unittest.main()
