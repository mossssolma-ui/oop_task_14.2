import json
import os

from src.categories import Category
from src.products import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data  # type: ignore


def create_objects_from_json(data: dict) -> list:
    category = []
    for cat in data:
        prod = []
        for pr in cat["products"]:
            prod.append(Product(**pr))
        cat["products"] = prod
        category.append(Category(**cat))
    return category


# if __name__ == "__main__":
#     data = read_json("../data/products.json")
#     category = create_objects_from_json(data)
#
#     result: dict = {}
#     for i in range(len(category)):
#         obj = category[i]
#         result[obj.name] = []
#         for j in obj.products:
#             result[obj.name].append(j.name)
#
#     print(json.dumps(result, ensure_ascii=False, indent=4))
