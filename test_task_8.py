from playwright.sync_api import Page, expect

from main import BASE_URL


def test_hover_effect(page: Page):
    page.goto(BASE_URL + "/hovers")
    first_figure = page.locator(".figure").first
    first_figure.hover()
    name_text = first_figure.locator("figcaption > h5")
    expect(name_text).to_be_visible()
    actual_name = name_text.inner_text()
    print(f"✅ Навели на изображение. Текст: {actual_name.strip()}")