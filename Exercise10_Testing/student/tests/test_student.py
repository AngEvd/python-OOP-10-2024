import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Test")
        self.student_with_courses = Student("Test1", {"OOP": ["September"]})

    def test_init(self):
        self.assertEqual(self.student.name, "Test")
        self.assertEqual(self.student.courses, {})

        self.assertEqual(self.student_with_courses.name, "Test1")
        self.assertEqual(self.student_with_courses.courses, {"OOP": ["September"]})

    def test_enroll_same_course(self):
        result = self.student_with_courses.enroll("OOP", ["October"])
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(self.student_with_courses.courses, {"OOP": ["September", "October"]})

    def test_enroll_new_course_with_no_course_notes(self):
        result = self.student.enroll("OOP", ["September"])
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses, {"OOP": ["September"]})

    def test_enroll_new_course_with_Y_course_notes(self):
        result = self.student.enroll("OOP", ["September"], "Y")
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses, {"OOP": ["September"]})

    def test_enroll_new_course_with_course_notes(self):
        result = self.student.enroll("OOP", ["September"], "Additional notes")
        self.assertEqual(result, "Course has been added.")
        self.assertEqual(self.student.courses, {"OOP": []})

    def test_add_noted_enrolled_course(self):
        result = self.student_with_courses.add_notes("OOP", "December")
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(self.student_with_courses.courses, {"OOP": ["September", "December"]})

    def test_add_noted_not_enrolled_course(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes("OOP", "December")
        self.assertEqual(str(context.exception), "Cannot add notes. Course not found.")

    def test_leave_enrolled_course(self):
        result = self.student_with_courses.leave_course("OOP")
        self.assertEqual(result, "Course has been removed")
        self.assertEqual(self.student_with_courses.courses, {})

    def test_leave_not_enrolled_course(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course("OOP")
        self.assertEqual(str(context.exception), "Cannot remove course. Course not found.")


if __name__ == "__main__":
    unittest.main()




