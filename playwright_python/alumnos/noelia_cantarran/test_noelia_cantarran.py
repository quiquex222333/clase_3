import re
from playwright.sync_api import Page, expect

# ======= TESTS SIMPLES =======

def test_simple_pass():
    assert 10 > 5

def test_simple_fail():
    assert 5 > 10, "El test falla porque 5 no es mayor que 10"

# ======= TESTS CON WIKIPEDIA =======

def test_wikipedia_title(page: Page):
    page.goto("https://www.wikipedia.org/")
    # Verificar que el título contenga "Wikipedia"
    expect(page).to_have_title(re.compile("Wikipedia"))

def test_search_input_visible(page: Page):
    page.goto("https://www.wikipedia.org/")
    # Verificar que el input de búsqueda sea visible
    expect(page.locator("input#searchInput")).to_be_visible()

def test_search_for_playwright(page: Page):
    page.goto("https://www.wikipedia.org/")
    # Escribir "Playwright" en el buscador y presionar Enter
    page.fill("input#searchInput", "Playwright")
    page.press("input#searchInput", "Enter")
    # Verificar que el título de la página contenga "Playwright"
    expect(page).to_have_title(re.compile("Playwright"))

def test_first_heading(page: Page):
    page.goto("https://en.wikipedia.org/wiki/Playwright")
    # Verificar que el primer heading sea "Playwright"
    expect(page.locator("h1#firstHeading")).to_have_text("Playwright")
