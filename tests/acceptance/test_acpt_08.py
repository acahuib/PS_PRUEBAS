from playwright.sync_api import Page, expect
import re


def test_acpt_08(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    page.get_by_role("link", name="Measurements").click()
    page.goto("https://ps-pruebas.onrender.com/weight/add/")
    page.get_by_role("spinbutton", name="Weight").fill("5.5")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_role("cell", name="5.5")).to_be_visible()
