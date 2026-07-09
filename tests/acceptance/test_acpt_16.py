from playwright.sync_api import Page, expect
import re


def test_acpt_16(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    page.get_by_role("textbox", name="Username").fill("user")
    page.get_by_role("textbox", name="Password").fill("passuser1")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Recent Pumpings").click()
    page.get_by_role("link", name="Añadir extracción").click()
    page.get_by_role("spinbutton", name="Cantidad").click()
    page.get_by_role("spinbutton", name="Cantidad").fill("5")
    page.get_by_role("button", name="Enviar").click()
    expect(page.get_by_text("¡Entrada de Extracciones para")).to_be_visible()
