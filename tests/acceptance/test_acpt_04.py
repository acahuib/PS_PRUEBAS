from playwright.sync_api import Page, expect
import re


def test_acpt_04(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    page.get_by_role("link", name="Last Diaper Change").click()
    page.get_by_role("link", name="Add Diaper Change").click()
    page.get_by_text("Wet").click()
    page.get_by_text("Green").click()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Diaper Change entry for Juan")).to_be_visible()
