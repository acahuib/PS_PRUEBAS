from playwright.sync_api import Page, expect
import re


def test_acpt_03(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    page.get_by_role("link", name="Last Feeding", exact=True).click()
    page.get_by_role("link", name="Add Bottle Feeding").click()
    page.get_by_text("Formula").click()
    page.get_by_role("spinbutton", name="Amount").click()
    page.get_by_role("spinbutton", name="Amount").fill("4.5")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Feeding entry for Juan Perez")).to_be_visible()
