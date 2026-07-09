from playwright.sync_api import Page, expect
import re


def test_acpt_17(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    page.get_by_role("textbox", name="Username").fill("user")
    page.get_by_role("textbox", name="Password").fill("passuser1")
    page.get_by_role("button", name="Login").click()
    page.locator("#nav-children-menu-link").click()
    page.locator("#nav-children-menu-link").click()
    page.locator("#nav-children-menu-link").click()
    page.locator("#nav-children-menu-link").click()
    page.locator("#nav-children-menu-link").click()
    page.locator("#nav-children-menu-link").dblclick()
    page.locator("#nav-children-menu-link").dblclick()
    page.get_by_role("link", name="Nota", exact=True).click()
    page.get_by_role("textbox", name="Nota").click()
    page.get_by_role("textbox", name="Nota").press("CapsLock")
    page.get_by_role("textbox", name="Nota").fill("S")
    page.get_by_role("textbox", name="Nota").press("CapsLock")
    page.get_by_role("textbox", name="Nota").fill("Se intento parar")
    page.get_by_role("button", name="Enviar").click()
    expect(page.get_by_text("¡Entrada de Nota para Juan")).to_be_visible()
