from playwright.async_api import async_playwright, Page

from main import BASE_URL


def test_checkboxes(page :Page) -> None:
    page.goto(BASE_URL) + "/checkboxes"
    checkboxes  = page.locator("#checkboxes input")
    check1 = che
