# self_return_shape.py
from typing import Self, final

# Case 1: the Shape class has methods that return Self
# but instead, they return Shape() type. this should 
# throw errors. 
# why should it throw errors? 
# if Shape is subclassed by some other class Circle(Shape)
# and we do Circle.cls_method(cls), it returns a Shape type
# and not a Circle type, which is bad. this is why pyrefly
# is expected to throw errors in such scnearios.
class Shape:
    def method(self) -> Self:
        return Shape()  # this should throw an error

    @classmethod
    def cls_method(cls) -> Self:
        return Shape()  # this should throw an error

# Case 2: FinalShape is a final class, in this case the
# errors with return types Self can return FinalShape()
# as FinalShape is final, it cannot be subclassed and 
# these methods won't be expected to return some other
# concrete type
@final
class FinalShape:
    def method(self) -> Self:
        return FinalShape() 

    @classmethod
    def cls_method(cls) -> Self:
        return FinalShape() 
