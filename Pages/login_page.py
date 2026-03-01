class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "button:has-text('Login')"
        self.error_message = ".error-message"
        self.logout_link = "text=Logout"

    def navigate(self):
        self.page.goto("https://vinodsautomationshop.netlify.app/")

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        return self.page.locator(self.error_message).inner_text()

    def logout(self):
        self.page.click(self.logout_link)