from playwright.async_api import Page
from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://the-internet.herokuapp.com/"
EXAMPLE_NAME = "Form Authentication"
login = "/login"
exit = "/exit"
checkbox = "/checkbox"

def navigate_to_example(page, example_name: str) -> str:

    link = page.get_by_role("link", name=example_name)
    link.click()

    page.wait_for_load_state("networkidle")

    return page.url

# task number 2
def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_page()
        context.goto(BASE_URL)

        page_title = context.title()
        if "the-internet" in page_title.lower():
            h1_text = context.locator("h1").inner_text()
            print(f" Сайт доступен. Заголовок: {h1_text}")

        print(f"Переходим в раздел: {EXAMPLE_NAME}...")
        current_url = navigate_to_example(context, EXAMPLE_NAME)

        if "/login" in current_url:
            print(f" Перешли в: {EXAMPLE_NAME} | URL: {current_url}")
        else:
            print(f" Ошибка навигации. Текущий URL: {current_url}")

        browser.close()

#task number 3
def test_login_form(page:Page):
    page.goto(BASE_URL)
    page.url + "/login"
    page.fill("username", "tomsmith")
    page.fill("password", "SuperSecretPassword!")
    page.get_by_role("link", name="login").click()
    expect(page).to_have_url(BASE_URL)
    page.url = BASE_URL + "/secure"
    print("✅ Успешный вход! URL: /secure")


# task number 4
def test_loginout(page:Page):
    page.goto(BASE_URL)
    page.url + "/login"
    page.get_by_text("Logout").click()
    expect(page).to_have_url(BASE_URL)
    print(f"✅ Успешный выход! URL: {page.url}")






if __name__ == "__main__":
    run_test()

