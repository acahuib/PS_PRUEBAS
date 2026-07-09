from playwright.sync_api import Page, expect
import re


def test_acpt_20(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    page.get_by_role("textbox", name="Username").fill("user")
    page.get_by_role("textbox", name="Password").fill("passuser1")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Mediciones").click()
    page.goto("https://ps-pruebas.onrender.com/height/add/")
    page.get_by_role("spinbutton", name="Altura").fill("57")
    page.get_by_role("button", name="Enviar").click()
    expect(page.get_by_text("¡Entrada de Altura para Juan")).to_be_visible()
