from playwright.sync_api import Page, expect
import re


def test_acpt_12(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    page.get_by_role("link", name="anthony leonel").click()
    page.get_by_role("link", name="Settings").click()
    page.get_by_label("Language").select_option("es")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("¡Configuraciones guardadas!")).to_be_visible()
