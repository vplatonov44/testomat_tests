class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("/users/sign_in")
