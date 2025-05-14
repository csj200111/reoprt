from exceptions import ProductNotFoundException

class ProductCatalog:
    def __init__(self):
        self.products = {
            "무선 이어폰": 10000,
            "스마트워치": 20000
        }

    def get_price(self, product_name):
        if product_name not in self.products:
            raise ProductNotFoundException(f"상품 '{product_name}'을 찾을 수 없습니다.")
        return self.products[product_name]
