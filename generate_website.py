import products
import store

# Sample products
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
    products.NonStockedProduct("Windows License", price=125),
    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
]

# Creating the store
best_buy = store.Store(product_list)

#  HTML template
with open("static/index_template.html", "r") as template_file:
    html_template = template_file.read()

# Creating the HTML block for each product
product_html_blocks = ""
for product in best_buy.get_all_products():
    promotion_text = ""
    if product.get_promotion():
        promotion_text = f"<p class='promo'>Promotion: {product.get_promotion().name}</p>"

    product_html_blocks += f"""
    <li class="product-card">
        <div class="product-content">
            <h2>{product.name}</h2>
            <p><strong>Price:</strong> ${product.price}</p>
            <p><strong>Quantity:</strong> {'∞' if product.quantity == 0 else product.quantity}</p>
            <p><strong>Type:</strong> {type(product).__name__}</p>
            {promotion_text}
        </div>
    </li>
    """

#  placeholders
html_filled = html_template.replace("__TEMPLATE_TITLE__", "Best Buy 2.0 - Product Catalog")
html_filled = html_filled.replace("__TEMPLATE_MOVIE_GRID__", product_html_blocks)

# Writing to index.html
with open("static/index.html", "w") as output_file:
    output_file.write(html_filled)

print("✅ HTML website generated: static/index.html")
