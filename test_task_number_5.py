from playwright.sync_api import Page, expect

from main import BASE_URL


def test_checkboxes(page: Page):

    checkboxes = page.locator("#checkboxes input")
    page.goto(BASE_URL + "/checkboxes")


    check1 = checkboxes.nth(0)
    check2 = checkboxes.nth(1)

    expect(check1).not_to_be_checked()
    expect(check2).to_be_checked()
    check1.check()
    check2.uncheck()
    print(f"✅ Checkbox 1: checked={check1.is_checked()}")
    print(f"✅ Checkbox 2: checked={check2.is_checked()}")