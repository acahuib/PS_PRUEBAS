from playwright.sync_api import Page, expect
import re


def test_acpt_11(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    page.get_by_role("link", name="Measurements").click
    page.goto("https://ps-pruebas.onrender.com/weight/add/")
    page.get_by_role("textbox", name="Date").fill("2026-07-01")
    page.get_by_role("spinbutton", name="Weight").fill("4")
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("link", name="Timeline").click()
    page.get_by_role("link", name="Reports").click()
    page.get_by_role("link", name="Weight", exact=True).click()
    expect(page.locator("rect").nth(4)).to_be_visible()
