from playwright.sync_api import Page, expect
import re


def test_acpt_05(page: Page):
    page.goto("https://ps-pruebas.onrender.com/")
    page.get_by_role("link", name="Last Sleep").click()
    page.get_by_role("link", name="Add Sleep").click()
    page.get_by_role("textbox", name="Start time").fill("2026-07-08T14:00:30")
    page.get_by_role("textbox", name="End time").fill("2026-07-08T18:02:50")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Sleep entry for Juan Perez")).to_be_visible()
