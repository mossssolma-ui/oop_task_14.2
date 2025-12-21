from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс продукта"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):  # type: ignore
        """Абстрактный метод нового продукта"""
        ...
