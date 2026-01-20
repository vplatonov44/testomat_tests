from playwright.sync_api import Page, expect


def test_login_with_invalid_creds(page: Page):
    page.goto("https://testomat.io")

    expect(page.locator("[href*='sign_in'].login-item")).to_be_visible()

    expect(page.get_by_text("Log in", exact=True)).to_be_visible()

    page.get_by_text("Log in", exact=True).click()

    # page.get_by_role("textbox", name="name@email.com")
    page.locator("#content-desktop #user_email").fill("ceopltn@gmail.com")
    page.locator("#content-desktop #user_password").fill("asddad")
    page.get_by_role("button", name="Sign in").click()

    expect(page.locator("#content-desktop").get_by_text("Invalid Email or password.")).to_be_visible()
    expect(page.locator("#content-desktop .common-flash-info")).to_have_text("Invalid Email or password.")


def test_search_project_in_company(page: Page):
    page.goto("https://testomat.io")

    page.get_by_text("Log in", exact=True).click()

    page.locator("#content-desktop #user_email").fill("ceopltn@gmail.com")
    page.locator("#content-desktop #user_password").fill("N3jtenjzpR6otQ")
    page.get_by_role("button", name="Sign in").click()

    target_project = "Manufacture light"
    expect(page.get_by_role("searchbox", name="Search")).to_be_visible()
    page.locator("#content-desktop #search").fill(target_project)

    expect(page.get_by_role("heading", name=target_project).first).to_be_visible()
