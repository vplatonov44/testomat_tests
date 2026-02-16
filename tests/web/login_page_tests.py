from playwright.sync_api import Page

from src.web.pages.HomePage import HomePage


def test_login_page(page: Page):
    HomePage(page).open()
