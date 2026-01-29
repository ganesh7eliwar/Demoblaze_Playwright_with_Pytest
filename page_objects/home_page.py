from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.all_products = self.page.locator('div#tbodyid div.card h4.card-title a')
        self.add_to_cart_button = self.page.locator('//a[normalize-space()="Add to cart"]')
        self.cart_link = self.page.locator('#cartur')

    def add_product(self, product_name):

        products = self.all_products.all()

        for product in products:
            item_name = product.text_content().strip()
            # print(item_name)

            if item_name == product_name:
                product.click()
                break

        self.page.on('dialog', lambda dialog: dialog.accept())
        self.add_to_cart_button.click()

    def goto_cart(self):
        self.cart_link.click()
