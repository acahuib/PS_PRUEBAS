import os
import subprocess
import pytest

STATE_FILE = os.path.join(os.path.dirname(__file__), "state.json")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    # Generar state.json ejecutando el script standalone
    if not os.path.exists(STATE_FILE):
        script_path = os.path.join(os.path.dirname(__file__), "setup_login.py")
        subprocess.run(["python3", script_path], check=True)

    return {
        **browser_context_args,
        "storage_state": STATE_FILE,
    }
