import unittest

from shapes import Square, Circle, draw_shape


class TestCircle(unittest.TestCase):
    def setUp(self) -> None:
        self.circle = Circle([-10, 11], 3)

    def test_area(self):
        area = self.circle.get_area()
        self.assertAlmostEqual(area, 28.27, places=2)

    def test_circle_name(self):
        name = self.circle.get_name()
        self.assertEqual(name, "Circle")

    def test_setcolor(self):
        self.circle.set_color("yellow")
        self.assertEqual(self.circle.get_color(), "yellow")

class TestSquare(unittest.TestCase):
    def setUp(self) -> None:
        self.square = Square([0, 5], 5)

    def test_square_area(self):
        area = self.square.get_area()
        self.assertEqual(area, 25)

    def test_square_name(self):
        name = self.square.get_name()
        self.assertEqual(name, "Square")


    def test_setcolor(self):
        self.square.set_color("pink")
        self.assertEqual(self.square.get_color(), "pink")

    # def test_perimeter_square(self):
    #     perimeter = self.square.get_perimeter()
    #     self.assertEqual(perimeter, 20)

    # def test_perimeter_circle(self):
    #     perimeter = self.circle.get_perimeter()
    #     self.assertEqual(perimeter, 18.84)
        

if __name__ == "__main__":
    unittest.main()
