from typing import Self, final


# Case 1: the Shape class has methods that return Self but instead, they
# return Shape() type. this should throw errors. why should it throw errors?
# if Shape is subclassed by some other class Circle(Shape) and we do
# Circle.cls_method(cls), it returns a Shape type and not a Circle type,
# which is bad. this is why pyrefly is expected to throw errors in such
# scnearios.
class Shape:
    # this should throw an error
    def method(self) -> Self:
        return Shape()

    # this should throw an error
    @classmethod
    def cls_method(cls) -> Self:
        return Shape()


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

# Case 3: GoodShape has a cls_method which returns an
# instance of the runtime class. so this should be fine
# as when GoodShape is subclassed by AmazingShape(GoodShape),
# AmazingShape.cls_method() returns AmazingShape(), which is
# fine.
class GoodShape:
    @classmethod
    def cls_method(cls) -> Self:
        return cls()


class ShapeFactory:
    # expect error as it is clas, not instance
    @classmethod
    def cls_method(cls) -> Self:
        return cls

    # expect error as self is unknown
    @classmethod
    def another_cls_method(cls) -> Self:
        return self

    # expect error as self is unknown
    @staticmethod
    def some_static_method() -> Self:
        return self

failures:
    test::callable::test_constructor_callable_conversion
    test::constructors::test_constructor_typevar_scope_overload
    test::constructors::test_generic_in_generic
    test::constructors::test_init_overload_with_self
    test::constructors::test_overloaded_init
    test::descriptors::test_bound_method_preserves_function_attributes_from_descriptor
    test::generic_basic::test_functools_partial_pattern
    test::overload::test_constructor_overload_with_hint