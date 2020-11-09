class Shop:

    total_sales = 0

    def __init__(self, shop_name, sales):
        self.sales = sales
        self.shop_name = shop_name
        #Shop.total_sales += sales
        self.__class__.total_sales += sales

    def make_sales(self, sales):
        self.sales += sales
        Shop.total_sales += sales

    # @staticmethod
    # def get_total_sales():
    #     if Shop.total_sales < 1000:
    #         return ('Sales are bad', Shop.total_sales)
    #     return ('Sales are good', Shop.total_sales)

    @classmethod
    def get_total_sales(cls):
        if cls.total_sales < 1000:
            return ('Sales are bad', cls.total_sales)
        return ('Sales are good', cls.total_sales)


print(Shop.get_total_sales())