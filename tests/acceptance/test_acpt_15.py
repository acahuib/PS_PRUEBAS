from playwright.sync_api import Page, expect
import re


def test_acpt_15(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    page.get_by_role("textbox", name="Username").fill("user")
    page.get_by_role("textbox", name="Password").fill("passuser1")
    page.get_by_role("button", name="Login").click()
    page.locator("#nav-children-menu-link").click()
    page.get_by_label("Niños").get_by_role("link", name="Niños").click()
    page.locator(".btn.btn-warning").click()
    page.get_by_role("textbox", name="Nombre").click()
    page.get_by_role("textbox", name="Nombre").fill("Juan")
    page.get_by_role("textbox", name="Nombre").press("CapsLock")
    page.get_by_role("textbox", name="Nombre").fill("JuanED")
    page.get_by_role("textbox", name="Nombre").press("CapsLock")
    page.get_by_role("textbox", name="Nombre").fill("Juan ")
    page.get_by_role("textbox", name="Nombre").press("CapsLock")
    page.get_by_role("textbox", name="Nombre").fill("Juan E")
    page.get_by_role("textbox", name="Nombre").press("CapsLock")
    page.get_by_role("textbox", name="Nombre").fill("Juan Editado")
    page.get_by_role("button", name="Enviar").click()
    expect(page.get_by_text("Niño entrada actualizada.")).to_be_visible()
