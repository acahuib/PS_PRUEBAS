from playwright.sync_api import Page, expect
import re


def test_acpt_09(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    page.locator("#dashboard-child").get_by_role("link", name="Timers").click()
    page.get_by_role("link", name="Start Timer").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").press("CapsLock")
    page.get_by_role("textbox", name="Name").fill("P")
    page.get_by_role("textbox", name="Name").press("CapsLock")
    page.get_by_role("textbox", name="Name").fill("Prueba")
    page.get_by_role("textbox", name="Name").press("CapsLock")
    page.get_by_role("textbox", name="Name").press("CapsLock")
    page.get_by_role("textbox", name="Name").press("CapsLock")
    page.get_by_role("textbox", name="Name").fill("PruebaT")
    page.get_by_role("textbox", name="Name").press("CapsLock")
    page.get_by_role("textbox", name="Name").fill("PruebaTimer")
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("button", name="Pumping").click()
    page.get_by_role("spinbutton", name="Amount").click()
    page.get_by_role("spinbutton", name="Amount").fill("2")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Pumping entry for Juan Perez")).to_be_visible()
    page.get_by_role("link", name="Dashboard").click()
    expect(page.get_by_text("0 timers")).to_be_visible()
