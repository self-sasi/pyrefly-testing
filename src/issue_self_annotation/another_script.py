from typing import Self

class SomeClass:

    def some_method(self) -> Self:
        return self
    
    @classmethod
    def another_method(cls) -> Self:
        return cls()
