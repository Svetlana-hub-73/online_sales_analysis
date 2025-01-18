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
from cart import Cart

# Kreiranje korpe
cart = Cart()
cart.add_to_cart(product1)
cart.add_to_cart(product2)

# Prikaz sadržaja korpe
cart.display_cart()
print(f"Total cart value: ${cart.calculate_total()}")

