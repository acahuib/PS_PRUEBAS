from playwright.sync_api import Page, expect
import re


def test_acpt_02(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    page.get_by_role("link", name="Add a Child").click()
    page.get_by_role("textbox", name="First name").click()
    page.get_by_role("textbox", name="First name").fill("")
    page.get_by_role("textbox", name="First name").press("CapsLock")
    page.get_by_role("textbox", name="First name").fill("J")
    page.get_by_role("textbox", name="First name").press("CapsLock")
    page.get_by_role("textbox", name="First name").fill("Juan")
    page.get_by_role("textbox", name="First name").press("Tab")
    page.get_by_role("textbox", name="Last name").press("CapsLock")
    page.get_by_role("textbox", name="Last name").fill("P")
    page.get_by_role("textbox", name="Last name").press("CapsLock")
    page.get_by_role("textbox", name="Last name").fill("Perez")
    page.get_by_role("textbox", name="Birth date").fill("2026-03-10")
    page.get_by_role("textbox", name="Birth time").fill("19:42")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_role("link", name="Juan")).to_be_visible()
