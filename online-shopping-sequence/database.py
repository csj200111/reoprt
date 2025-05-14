class Database:
    def __init__(self):
        self.orders = []

    def save_order(self, user, product_name, price):
        print(f"[Database] '{user}'의 주문 저장됨: {product_name} ({price}원)")
        self.orders.append({
            "user": user,
            "product": product_name,
            "price": price
        })
