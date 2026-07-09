from playwright.sync_api import Page, expect
import re


def test_acpt_10(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    page.get_by_role("link", name="Activities").click()
    page.get_by_role("link", name="Activities").click()
    page.get_by_role("link", name="Activities").click()
    page.get_by_role("link", name="Activities").click()
    page.get_by_role("link", name="Activities").click()
    page.get_by_role("link", name="Medication").nth(1).click()
    page.get_by_role("spinbutton", name="Time Until Next Dosage").click()
    page.get_by_role("spinbutton", name="Time Until Next Dosage").fill("12")
    page.get_by_role("textbox", name="Medication Name").click()
    page.get_by_role("textbox", name="Medication Name").press("CapsLock")
    page.get_by_role("textbox", name="Medication Name").fill("I")
    page.get_by_role("textbox", name="Medication Name").press("CapsLock")
    page.get_by_role("textbox", name="Medication Name").fill("Ibuprofeno")
    page.get_by_role("spinbutton", name="Dosage", exact=True).click()
    page.get_by_role("spinbutton", name="Dosage", exact=True).fill("1")
    page.get_by_text("Tablets").click()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Medication entry for Juan")).to_be_visible()
    page.get_by_text("Medication entry for Juan").click()
