# main.py
from product_catalog import ProductCatalog
from payment_gateway import PaymentGateway
from database import Database
from shop_server import ShopServer
from ui import UI

catalog = ProductCatalog()
payment = PaymentGateway()
db = Database()
server = ShopServer(catalog, payment, db)
ui = UI(server)

# 정상 케이스
ui.purchase("세진", "무선 이어폰", "카드1234")

# 상품 없음
ui.purchase("세진", "노트북", "카드1234")

# 결제 실패
ui.purchase("세진", "스마트워치", "declined-card")
