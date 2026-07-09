import pytest


@pytest.fixture
def browser_context_args(browser_context_args):
    return {k: v for k, v in browser_context_args.items() if k != "storage_state"}


# Archivo: tests/acceptance/test_acpt_01_login.py

from playwright.sync_api import Page, expect


# La función DEBE empezar con la palabra "test_"
def test_login_exitoso(page: Page):

    # --- SOLO COPIAMOS LA CARNE DE LA PRUEBA ---
    page.goto("https://ps-pruebas.onrender.com/login/?next=/")
    page.get_by_role("textbox", name="Username").fill("user")
    page.get_by_role("textbox", name="Password").fill("passuser1")
    page.get_by_role("button", name="Login").click()

    # Nuestra aserción final
    expect(
        page.locator("div").filter(has_text="Welcome to Baby Buddy! Learn").nth(3)
    ).to_be_visible()
