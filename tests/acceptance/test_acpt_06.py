from playwright.sync_api import Page, expect
import re


def test_acpt_06(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    expect(page.get_by_text("hours, 2 minutes, 20 seconds")).to_be_visible()
    page.goto("https://ps-pruebas.onrender.com/children/juan-perez/dashboard/")
