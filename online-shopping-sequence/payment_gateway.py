from exceptions import PaymentDeclinedException

class PaymentGateway:
    def authorize(self, card_info, amount):
        print(f"[PaymentGateway] '{amount}원' 결제 요청")
        if "declined" in card_info:
            raise PaymentDeclinedException("결제가 거절되었습니다.")
        return True
