from store import Store
from products import Product, NonStockedProduct, LimitedProduct
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount

def create_store():
    """
    Initializes and returns a Store instance with products and promotions.
    """
    # Setting up initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
    ]

    # Creating promotions
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Assigning promotions
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    return Store(product_list)


def print_menu():
    """
    Displays the user menu options.
    """
    print("\n   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")
    print("Please choose a number: ", end='')


def handle_list_products(store):
    """
    Lists all products in the store.
    """
    products = store.get_all_products()
    print("\n--- All Products ---")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.show()}")


def handle_total_quantity(store):
    """
    Displays the total quantity of all items in the store.
    """
    total = store.get_total_quantity()
    print(f"\nTotal items in store: {total}")


def handle_order(store):
    """
    Handles placing an order by selecting products and quantities.
    """
    cart = []
    products = store.get_all_products()

    print("\n--- Available Products ---")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.name} ({product.quantity} available)")

    print("Enter product number and quantity (e.g., 1,2). Leave blank to finish.")
    while True:
        user_input = input("Enter product and quantity: ")
        if not user_input.strip():
            break
        try:
            prod_num, quantity = map(int, user_input.split(","))
            selected_product = products[prod_num - 1]
            cart.append((selected_product, quantity))
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

    if not cart:
        print("No items selected.")
        return

    try:
        total_price = store.order(cart)
        print(f"\nOrder successful! Total price: ${total_price:.2f}")
    except Exception as e:
        print(f"Order failed: {e}")


def main():
    """
    Entry point for the Best Buy 2.0 application.
    """
    store = create_store()

    while True:
        print_menu()
        choice = input()
        if choice == '1':
            handle_list_products(store)
        elif choice == '2':
            handle_total_quantity(store)
        elif choice == '3':
            handle_order(store)
        elif choice == '4':
            print("Thanks for shopping with Best Buy 2.0!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
