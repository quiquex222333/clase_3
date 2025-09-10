import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://bookcreator.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Book"))


def test_create_free_account_button(page: Page):
    # Abrir la página principal
    page.goto("https://bookcreator.com/")

    # Seleccionar el botón por su texto
    button = page.get_by_role("link", name="Create a FREE account").first

    # Verificar que sea visible
    expect(button).to_be_visible()