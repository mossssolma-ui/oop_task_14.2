class Product:
    """Класс описывает карточку продукта"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация экземпляра продукта"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Возвращает текущую цену продукта"""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Устанавливает новую цену продукта > 0"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if hasattr(self, "_Product__price"):
            if value < self.__price:
                user_choice = input(
                    f"Вы хотите понизить цену с {self.__price} до {value}? Введите 'y' для подтверждения: "
                )
                if user_choice.lower() != "y":
                    print("Отмена\n")
                    return

        self.__price = value

    @classmethod
    def new_product(cls, product_data: dict, products_list: list["Product"] | None = None) -> Product:
        """
        Создает новый продукт из словаря данных
        Также, если в переданном списке продуктов products_list уже
        существует товар с таким же названием,
        то в исходном товаре увеличивается количество,
        и записывается большая цена
        """
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        if products_list:
            for product in products_list:
                if product.name == name:
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
                    return product

        return cls(name, description, price, quantity)
