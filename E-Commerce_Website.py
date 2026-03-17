import json
import os
import datetime

USERS_FILE  = "users.json"
CARTS_FILE  = "carts.json"
ORDERS_FILE = "orders.json"

# ---------- Load & Save ----------
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}

def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

users        = load_data(USERS_FILE)
carts        = load_data(CARTS_FILE)
orders       = load_data(ORDERS_FILE)
current_user = None

# ---------- Product Database ----------
products = {
    1:  {"name": "Dell Inspiron Laptop",        "price": 58000,  "category": "Electronics"},
    2:  {"name": "HP Pavilion Laptop",           "price": 62000,  "category": "Electronics"},
    3:  {"name": "Asus Vivobook",                "price": 54000,  "category": "Electronics"},
    4:  {"name": "Lenovo ThinkPad",              "price": 72000,  "category": "Electronics"},
    5:  {"name": "Apple MacBook Air M2",         "price": 118000, "category": "Electronics"},
    6:  {"name": "iPhone 15 Pro",                "price": 135000, "category": "Mobiles"},
    7:  {"name": "Samsung Galaxy S24",           "price": 88000,  "category": "Mobiles"},
    8:  {"name": "OnePlus 12R",                  "price": 42000,  "category": "Mobiles"},
    9:  {"name": "Redmi Note 13 Pro",            "price": 24000,  "category": "Mobiles"},
    10: {"name": "Realme Narzo 70",              "price": 18000,  "category": "Mobiles"},
    11: {"name": "Boat Airdopes 441",            "price": 2500,   "category": "Accessories"},
    12: {"name": "JBL Headphones",               "price": 4200,   "category": "Accessories"},
    13: {"name": "Logitech Wireless Mouse",      "price": 900,    "category": "Accessories"},
    14: {"name": "Cosmic Byte Gaming Keyboard",  "price": 2900,   "category": "Accessories"},
    15: {"name": "Sony Bluetooth Speaker",       "price": 5200,   "category": "Accessories"},
    16: {"name": "PlayStation 5",                "price": 58990,  "category": "Gaming"},
    17: {"name": "Xbox Series X",                "price": 55000,  "category": "Gaming"},
    18: {"name": "Oculus VR Headset",            "price": 27000,  "category": "Gaming"},
    19: {"name": "Razer Gaming Mouse",           "price": 3500,   "category": "Gaming"},
    20: {"name": "Gaming Chair",                 "price": 18000,  "category": "Gaming"},
    21: {"name": "Levi's Denim Jacket",          "price": 4500,   "category": "Fashion"},
    22: {"name": "Nike Air Max Shoes",           "price": 9000,   "category": "Fashion"},
    23: {"name": "Adidas Track Pants",           "price": 3500,   "category": "Fashion"},
    24: {"name": "Puma T-Shirt",                 "price": 2200,   "category": "Fashion"},
    25: {"name": "Ray-Ban Sunglasses",           "price": 6800,   "category": "Fashion"},
    26: {"name": "Philips Mixer Grinder",        "price": 3800,   "category": "Home"},
    27: {"name": "Prestige Pressure Cooker",     "price": 2400,   "category": "Home"},
    28: {"name": "Bajaj Electric Kettle",        "price": 1600,   "category": "Home"},
    29: {"name": "Ceiling Fan Crompton",         "price": 3000,   "category": "Home"},
    30: {"name": "LED Bulb Pack",                "price": 800,    "category": "Home"},
    31: {"name": "Python Programming Book",      "price": 650,    "category": "Books"},
    32: {"name": "Data Structures & Algorithms", "price": 800,    "category": "Books"},
    33: {"name": "Atomic Habits",                "price": 500,    "category": "Books"},
    34: {"name": "Rich Dad Poor Dad",            "price": 450,    "category": "Books"},
    35: {"name": "The Alchemist",                "price": 400,    "category": "Books"},
    36: {"name": "Fortune Sunflower Oil 1L",     "price": 180,    "category": "Grocery"},
    37: {"name": "Aashirvaad Atta 10kg",         "price": 520,    "category": "Grocery"},
    38: {"name": "Tata Salt 1kg",                "price": 25,     "category": "Grocery"},
    39: {"name": "Red Label Tea 500g",           "price": 260,    "category": "Grocery"},
    40: {"name": "Bru Coffee 200g",              "price": 220,    "category": "Grocery"},
    41: {"name": "SG Cricket Bat",               "price": 1800,   "category": "Sports"},
    42: {"name": "Yonex Badminton Racket",       "price": 2300,   "category": "Sports"},
    43: {"name": "Nivia Football",               "price": 1200,   "category": "Sports"},
    44: {"name": "Gym Dumbbells Set",            "price": 3500,   "category": "Sports"},
    45: {"name": "Yoga Mat",                     "price": 900,    "category": "Sports"},
    46: {"name": "L'Oreal Shampoo",              "price": 280,    "category": "Beauty"},
    47: {"name": "Lakme Compact Powder",         "price": 250,    "category": "Beauty"},
    48: {"name": "Nivea Cream",                  "price": 180,    "category": "Beauty"},
    49: {"name": "Maybelline Lipstick",          "price": 550,    "category": "Beauty"},
    50: {"name": "Beardo Beard Oil",             "price": 400,    "category": "Beauty"},
}


def register():
    # BUG 7 FIX: validate empty username and password
    username = input("Enter username: ").strip()
    if not username:
        print("❌ Username cannot be empty!")
        return
    if username in users:
        print("❌ Username already exists!")
        return
    password = input("Enter password: ").strip()
    if not password:
        print("❌ Password cannot be empty!")
        return
    # BUG 1 FIX: store as dict, not plain string
    users[username]  = {"password": password}
    carts[username]  = []
    orders[username] = []
    save_data(USERS_FILE, users)
    save_data(CARTS_FILE, carts)
    save_data(ORDERS_FILE, orders)
    print("✅ Registration successful!")


def login():
    global current_user
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    stored = users.get(username)
    if stored is None:
        print("❌ Invalid credentials!")
        return
    # BUG 2 FIX: handle both dict format (new) and plain string (legacy)
    stored_pass = stored["password"] if isinstance(stored, dict) else stored
    if stored_pass == password:
        current_user = username
        print(f"✅ Welcome back, {username}!")
    else:
        print("❌ Invalid credentials!")


def logout():
    global current_user
    if current_user:
        print(f"👋 Logged out from {current_user}.")
        current_user = None
    else:
        print("⚠️  No user logged in.")


# ---------- Product Display ----------

def show_categories():
    categories = sorted(set(p["category"] for p in products.values()))
    print("\n📂 Categories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")


def show_products(category=None):
    print("\n🛒 Available Products")
    print("=" * 65)
    found = False
    for pid, item in products.items():
        if category and item["category"].lower() != category.lower():
            continue
        print(f"  ID:{pid:2d} | {item['name']:<32} ₹{item['price']:<8} | {item['category']}")
        found = True
    # BUG 9 FIX: show message if category has no results
    if not found:
        print(f"  ⚠️  No products found in category '{category}'.")
    print("=" * 65)


# ---------- Cart Operations ----------

def add_to_cart(pid):
    if not current_user:
        print("⚠️  Please login first!")
        return
    if pid not in products:
        print("❌ Invalid Product ID!")
        return
    # BUG 5 FIX: validate quantity input — catch ValueError + reject <= 0
    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("❌ Please enter a valid integer quantity.")
        return
    # BUG 8 FIX: reject zero or negative quantity
    if qty <= 0:
        print("❌ Quantity must be greater than 0.")
        return

    cart = carts[current_user]
    for item in cart:
        # BUG 3 FIX: cast item["id"] to int — JSON reload turns int keys to strings
        if int(item["id"]) == pid:
            item["quantity"] += qty
            break
    else:
        cart.append({"id": pid, "quantity": qty})
    save_data(CARTS_FILE, carts)
    print(f"✅ Added {qty} × {products[pid]['name']} to cart.")


def remove_from_cart(pid):
    if not current_user:
        print("⚠️  Please login first!")
        return
    cart = carts[current_user]
    # BUG 4 FIX: never mutate a list while iterating over it
    #            find the index first, then pop after the loop
    idx_to_remove = None
    for idx, item in enumerate(cart):
        if int(item["id"]) == pid:   # BUG 3 FIX: int() cast
            idx_to_remove = idx
            break
    if idx_to_remove is not None:
        cart.pop(idx_to_remove)
        save_data(CARTS_FILE, carts)
        print(f"🗑️  {products[pid]['name']} removed from cart.")
    else:
        print("❌ Item not found in cart!")


def show_cart():
    if not current_user:
        print("⚠️  Please login first!")
        return
    cart = carts[current_user]
    if not cart:
        print("\n🛒 Your cart is empty.")
        return
    total = 0
    print("\n🛒 Your Cart:")
    print("=" * 60)
    for i, item in enumerate(cart, 1):
        # BUG 3 FIX: int() cast before products lookup
        pid        = int(item["id"])
        qty        = item["quantity"]
        name       = products[pid]["name"]
        price      = products[pid]["price"]
        line_total = price * qty
        total     += line_total
        print(f"  {i}. {name:<32} ₹{price} × {qty} = ₹{line_total}")
    print("=" * 60)
    print(f"  Total Items : {len(cart)}")
    print(f"  Total Price : ₹{total}")
    print("=" * 60)


# ---------- Checkout + Order History ----------

def checkout():
    if not current_user:
        print("⚠️  Please login first!")
        return
    cart = carts[current_user]
    if not cart:
        print("❌ Your cart is empty!")
        return

    # BUG 3 FIX: int() cast on item["id"] for reliable lookup after JSON reload
    total        = sum(products[int(item["id"])]["price"] * item["quantity"] for item in cart)
    discount     = (0.20 if total > 100000 else
                    0.15 if total > 50000  else
                    0.10 if total > 20000  else
                    0.05 if total > 10000  else 0.00)
    discount_amt = round(total * discount, 2)
    gst          = round(0.18 * (total - discount_amt), 2)
    final_total  = round(total - discount_amt + gst, 2)

    order_id  = f"ORD{len(orders[current_user]) + 1:04d}"
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    order_data = {
        "order_id":    order_id,
        "date":        date_time,
        "items":       cart.copy(),
        "subtotal":    total,
        "discount":    discount_amt,
        "gst":         gst,
        "final_total": final_total,
    }
    orders[current_user].append(order_data)
    carts[current_user] = []
    save_data(ORDERS_FILE, orders)
    save_data(CARTS_FILE, carts)

    print("\n====== 🧾 BILL SUMMARY ======")
    print(f"  Order ID  : {order_id}")
    print(f"  Customer  : {current_user}")
    print(f"  Date      : {date_time}")
    print(f"  Subtotal  : ₹{total}")
    if discount > 0:
        print(f"  Discount  : ₹{discount_amt:.2f}  ({int(discount * 100)}% off)")
    print(f"  GST (18%) : ₹{gst:.2f}")
    print("  ------------------------------")
    print(f"  Final Amount to Pay : ₹{final_total:.2f}")
    print("==============================")
    print("✅ Thank you for shopping with us!")


def show_order_history():
    if not current_user:
        print("⚠️  Please login first!")
        return
    user_orders = orders.get(current_user, [])
    if not user_orders:
        print("\n📦 No previous orders found.")
        return
    print("\n📦 Order History:")
    print("=" * 70)
    for order in user_orders:
        print(f"  Order ID : {order['order_id']}  |  Date : {order['date']}")
        print(f"  Total    : ₹{order['final_total']:.2f}")
        print("  Items    :")
        for item in order["items"]:
            # BUG 3 FIX: int() cast for reliable product lookup after reload
            pid  = int(item["id"])
            qty  = item["quantity"]
            name = products[pid]["name"]
            print(f"    - {name} × {qty}")
        print("-" * 70)


# ---------- Main Menu ----------

def main():
    while True:
        print("\n========== 🛍️  E-Commerce Menu ==========")
        print("  1.  Register")
        print("  2.  Login")
        print("  3.  Logout")
        print("  4.  Show Categories")
        print("  5.  Show All Products")
        print("  6.  Browse by Category")
        print("  7.  Add to Cart")
        print("  8.  Remove from Cart")
        print("  9.  View Cart")
        print("  10. Checkout")
        print("  11. View Order History")
        print("  12. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            logout()
        elif choice == "4":
            show_categories()
        elif choice == "5":
            show_products()
        elif choice == "6":
            show_categories()
            cat = input("Enter category name: ").strip()
            show_products(cat)
        elif choice == "7":
            # BUG 6 FIX: validate Product ID input
            try:
                pid = int(input("Enter Product ID to add: "))
            except ValueError:
                print("❌ Please enter a valid product ID (number only).")
                continue
            add_to_cart(pid)
        elif choice == "8":
            # BUG 6 FIX: validate Product ID input
            try:
                pid = int(input("Enter Product ID to remove: "))
            except ValueError:
                print("❌ Please enter a valid product ID (number only).")
                continue
            remove_from_cart(pid)
        elif choice == "9":
            show_cart()
        elif choice == "10":
            checkout()
        elif choice == "11":
            show_order_history()
        elif choice == "12":
            print("👋 Exiting... Thank you for visiting our store!")
            break
        else:
            print("❌ Invalid choice! Please enter a number from 1 to 12.")


# BUG 10 FIX: wrap main loop so importing this file doesn't launch the menu
if __name__ == "__main__":
    main()