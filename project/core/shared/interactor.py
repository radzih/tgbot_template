from abc import ABC, abstractmethod
from typing import Any


class Interactor(ABC):
    @abstractmethod
    def __call__(self, data: Any) -> Any:
        ...
