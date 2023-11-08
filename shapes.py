import math
from typing import List


class Shape:
    position: List[float]
    _color: str = "blue"

    def __init__(self, position: List[float]):
        self.position = position
        
    def get_name(self) -> str:
        raise NotImplementedError

    def get_area(self) -> float:
        raise NotImplementedError

    def set_color(self, color: str):
        self._color = color

    def get_color(self) -> str:
        return self._color   
    

class Square(Shape):
    side_len: float

    def __init__(self, position: List[float], side_len: float):
        Shape.__init__(self, position)
        self.side_len = side_len

    def get_area(self) -> float:
        return self.side_len * self.side_len

    def get_name(self) -> str:
        return "Square"

                                    
class Circle(Shape):
    radius: float

    def __init__(self, position: List[float], radius: float):
        Shape.__init__(self, position)
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * self.radius * self.radius
                                    
    def get_name(self) -> str:
        return "Circle"
                                    
                                    
def draw_shape(shape: Shape) -> None:
    color = shape.get_color()
    name = shape.get_name()
    area = shape.get_area()
    x, y = shape.position
    print(f"Drawing a {color} {name} with area {area:.2f} at ({x}, {y})")
