from playwright.sync_api import Page, expect
import re


def test_acpt_07(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    page.get_by_role("link", name="Today's Tummy Time").click()
    page.get_by_role("link", name="Add Tummy Time").click()
    page.get_by_role("textbox", name="Start time").fill("2026-07-08T19:00:07")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Tummy Time entry for Juan")).to_be_visible()
