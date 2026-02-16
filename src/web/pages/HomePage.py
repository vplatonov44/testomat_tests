from playwright.sync_api import expect


class HomePage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://testomat.io")

    def is_loaded(self):
        expect(self.page.locator("#headerMenuWrapper")).to_be_visible()
        expect(self.page.locator(".login-item")).to_be_visible()
        expect(self.page.locator(".start-item")).to_be_visible()
