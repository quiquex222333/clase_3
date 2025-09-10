import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://www.youtube.com/")

    # Esperar que el título contenga "YouTube"
    expect(page).to_have_title(re.compile("YouTube"))

def test_search_function(page: Page):
    page.goto("https://www.youtube.com/")

    # Escribir algo en la barra de búsqueda
    page.get_by_role("combobox", name="Search").fill("Playwright Python")

    # Hacer clic en el botón de buscar
    page.get_by_role("button", name="Search").click()

    # Esperar que aparezcan resultados (verificar que hay un heading o algún video visible)
    expect(page.get_by_role("link").first).to_be_visible()