import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://duckduckgo.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("DuckDuckGo"))

def test_wikipedia_search(page: Page):
    # Abrir la página principal de Wikipedia
    page.goto("https://www.wikipedia.org/")

    # Escribir "Python" en la barra de búsqueda
    search_input = page.get_by_role("searchbox")
    search_input.fill("Python")

    # Presionar Enter para buscar
    search_input.press("Enter")

    # Verificar que el título contenga "Python"
    expect(page).to_have_title("Python - Wikipedia, la enciclopedia libre")

    # Verificar que el encabezado principal sea visible y tenga "Python"
    expect(page.get_by_role("heading", name="Python")).to_be_visible()

