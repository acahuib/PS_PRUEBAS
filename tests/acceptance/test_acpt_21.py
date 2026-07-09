from playwright.sync_api import Page, expect
import re


def test_acpt_21(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    page.get_by_role("textbox", name="Username").fill("user")
    page.get_by_role("textbox", name="Password").fill("passuser1")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Mediciones").click()
    page.goto("https://ps-pruebas.onrender.com/temperature/add/")
    page.get_by_role("spinbutton", name="Temperatura").click()
    page.get_by_role("spinbutton", name="Temperatura").fill("36.5")
    page.get_by_role("button", name="Enviar").click()
    expect(page.get_by_text("¡Entrada de Temperatura para")).to_be_visible()
