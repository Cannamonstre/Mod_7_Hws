from pprint import pprint


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, __file_name='products.txt'):
        self.__file_name = __file_name

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            with open(self.__file_name, 'w') as file:
                pass  # Creating file if it doesn't exist
            return ''  # Returning a string to have splitlines() method work correctly

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        existing_names = {line for line in existing_products}  # Using set comprehension for duplicates

        with open(self.__file_name, 'a') as file:
            for product in products:
                product_str = str(product)
                if product_str in existing_names:
                    print(f"Product {product.name} is already in the shop")
                else:
                    file.write(product_str + '\n')
                    existing_names.add(product_str)


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
