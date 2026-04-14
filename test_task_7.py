from playwright.sync_api import Page, expect

from main import BASE_URL


def test_input_field(page: Page):
    page.goto(BASE_URL + "/inputs")
    input_field = page.locator("input[type='number']")
    input_field.fill("123")
    expect(input_field).to_have_value("123")
    input_field.clear()
    input_field.fill("456")

    if input_field.input_value() == "456":
        print("✅ Введено: 456")