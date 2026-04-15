from playwright.sync_api import Page, expect

from main import BASE_URL


def test_dropdown_menu(page: Page):
    page.goto(BASE_URL + "/dropdown")

    dropdown = page.locator("#dropdown")
    expect(dropdown).to_have_value("")
    dropdown.select_option(label="Option 1")
    expect(dropdown).to_have_value("1")
    dropdown.select_option(label="Option 2")
    expect(dropdown).to_have_value("2")
    selected_text = page.eval_on_selector("#dropdown",
                                          "sel => sel.options[sel."
                                          "selectedIndex].text")
    print(f"✅ Выбрано: {selected_text}")