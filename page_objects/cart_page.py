from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.all_items_in_cart = self.page.locator('tbody#tbodyid tr td:nth-child(2)')

    def verify_item(self, product_name):

        products = self.all_items_in_cart.all()

        for product in products:
            item = product.text_content().strip()
            # print(item)

            if item == product_name:
                return product
        return None
