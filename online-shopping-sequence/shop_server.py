from exceptions import PaymentDeclinedException, ProductNotFoundException

class ShopServer:
    def __init__(self, catalog, payment, db):
        self.catalog = catalog
        self.payment = payment
        self.db = db

    def process_order(self, user, product_name, card_info):
        try:
            price = self.catalog.get_price(product_name)
            self.payment.authorize(card_info, price)
            self.db.save_order(user, product_name, price)
            return "✅ 결제 완료"
        except ProductNotFoundException as e:
            return f"❌ 상품 오류: {str(e)}"
        except PaymentDeclinedException as e:
            return f"❌ 결제 오류: {str(e)}"
