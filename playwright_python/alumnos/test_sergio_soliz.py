import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://www.facebook.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Facebook - log in or sign up"))

def test_get_started_link(page: Page):
    page.goto("https://www.youtube.com/")

    # Click en el botón de búsqueda
    page.get_by_role("button", name="Buscar").click()

    # Escribir algo en la barra de búsqueda
    page.get_by_role("combobox", name="Buscar").fill("Playwright Python")

    # Presionar Enter
    page.keyboard.press("Enter")

    # Validar que aparezcan resultados (por ejemplo que exista un enlace a un video)
    expect(page.get_by_role("link").first).to_be_visible()