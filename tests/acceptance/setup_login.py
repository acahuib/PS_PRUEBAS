import os
from playwright.sync_api import sync_playwright

STATE_FILE = os.path.join(os.path.dirname(__file__), "state.json")

if not os.path.exists(STATE_FILE):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://ps-pruebas.onrender.com/login/?next=/")
        page.get_by_role("textbox", name="Username").fill("user")
        page.get_by_role("textbox", name="Password").fill("passuser1")
        page.get_by_role("button", name="Login").click()
        try:
            page.wait_for_url("**/dashboard/**", timeout=30000)
        except Exception:
            pass
        context.storage_state(path=STATE_FILE)
        browser.close()
