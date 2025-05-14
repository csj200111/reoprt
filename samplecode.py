class PaymentGateway:
    def authorize_payment(self, card_info, amount):
        print("[PaymentGateway] 결제 승인 요청 중...")
        return True  # 항상 성공한다고 가정

class Database:
    def save_order(self, user, product):
        print(f"[Database] {user}의 '{product}' 주문 저장 완료")

class ShopServer:
    def __init__(self, payment_gateway, database):
        self.payment_gateway = payment_gateway
        self.database = database

    def process_order(self, user, product, card_info):
        print(f"[Server] '{product}' 주문 접수")
        approved = self.payment_gateway.authorize_payment(card_info, 10000)
        if approved:
            self.database.save_order(user, product)
            return "결제 완료"
        else:
            return "결제 실패"

class UI:
    def __init__(self, server):
        self.server = server

    def purchase_product(self, user, product, card_info):
        print(f"[UI] '{user}'가 '{product}' 결제 요청")
        result = self.server.process_order(user, product, card_info)
        print("[UI] 결제 결과:", result)

# 실행
payment = PaymentGateway()
db = Database()
server = ShopServer(payment, db)
ui = UI(server)

ui.purchase_product("세진", "무선 이어폰", "카드번호1234")

