from product import Product
from product_manager import ProductManager

# Kreiranje proizvoda
product1 = Product("Laptop", 1000, 5)
product2 = Product("Phone", 500, 10)

# Kreiranje ProductManager
manager = ProductManager()
manager.add_product(product1)
manager.add_product(product2)

# Prikaz proizvoda i ukupne vrednosti inventara
manager.display_products()
print(f"Total inventory value: ${manager.total_inventory_value()}")
