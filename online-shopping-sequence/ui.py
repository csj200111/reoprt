class UI:
    def __init__(self, server):
        self.server = server

    def purchase(self, user, product_name, card_info):
        print(f"[UI] {user}가 '{product_name}' 결제 시도")
        result = self.server.process_order(user, product_name, card_info)
        print(f"[UI] 결과: {result}")
