from playwright.sync_api import Page, expect
import re

import pytest


@pytest.fixture
def browser_context_args(browser_context_args):
    return {k: v for k, v in browser_context_args.items() if k != "storage_state"}


def test_acpt_13(page: Page):
    page.goto("https://ps-pruebas.onrender.com/login/")
    page.get_by_role("textbox", name="Username").fill("user")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("FALSA")
    page.get_by_role("button", name="Login").click()
    expect(
        page.get_by_text("Please enter a correct username and password")
    ).to_be_visible()
