class Shop:

    sold_by_all_shops = 0

    def __init__(self, name, items_sold):
        self.name = name
        self.items_sold = items_sold
        Shop.sold_by_all_shops += items_sold

    def print_shop_info(self):
        print(f'Shop -  {self.name}, total items sold - {self.items_sold}')

    def sell(self, items_amount):
        self.items_sold += items_amount
        Shop.sold_by_all_shops += items_amount
        print(f'{items_amount} items sold by {self.name}, {self.items_sold } in total')

    def print_total_sold_info():
        print(f'All shops sold {Shop.sold_by_all_shops} items')

Shop.print_total_sold_info()
shopA = Shop('A', 45)
shopA.sell(15)
shopA.sell(10)
Shop.print_total_sold_info()
shopB = Shop('B', 80)
shopA.sell(5)
shopA.sell(40)
shopA.sell(40)
Shop.print_total_sold_info()

