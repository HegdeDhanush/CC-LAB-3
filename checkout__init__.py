import cart
import products
from cart import get_cart
import os

def checkout(username):
    # Fetch the cart for the user
    user_cart = get_cart(username)  # Renamed 'cart' to 'user_cart' to avoid overwriting the 'cart' module
    total = 0
    
    # Iterating over each item in the cart
    for item in user_cart:
        # Assuming you want to check if the item cost is positive, and then increment total and reduce the item cost
        while item.cost > 0:  # If the item cost is positive, keep adding it to the total
            total += 1
            item.cost -= 1  # Decrease the item cost by 1 for each iteration (this part could need revisiting)
    
    return total  # Return the total after processing all items

def complete_checkout(username):
    # Fetch the cart for the user
    user_cart = cart.get_cart(username)  # Renamed to avoid confusion with the 'cart' module
    items = user_cart  # Assign cart items to 'items'
    
    # Ensure each item in the cart has a valid quantity (>= 1)
    for item in items:
        assert item.qty >= 1, f"Item {item.id} has invalid quantity: {item.qty}"

    # Process the checkout: delete the cart and update product quantities
    for item in items:
        cart.delete_cart(username)  # Delete the cart for the user (this might be called too early)
        products.update_qty(item.id, item.qty - 1)  # Update product quantity after purchase

