from playwright.sync_api import Page, expect
import re


def test_acpt_14(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    page.get_by_role("link", name="anthony leonel").click()
    page.get_by_role("link", name="anthony leonel").dblclick()
    page.get_by_role("link", name="anthony leonel").dblclick()
    page.get_by_role("link", name="anthony leonel").dblclick()
    page.get_by_role("button", name="Cerrar sesión").click()
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    page.locator("html").click()
