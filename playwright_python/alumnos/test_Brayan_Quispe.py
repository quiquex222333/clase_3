import re
from playwright.sync_api import Page, expect

def test_suma_basica():
    assert 2 + 2 == 4

def test_error_controlado():
    assert "QA" in "Playwright QA", "Texto esperado no encontrado"

def test_youtube_title(page: Page):
    page.goto("https://www.youtube.com/")
    expect(page).to_have_title(re.compile("YouTube"))

# Test de Google - validar campo de búsqueda
def test_google_search(page: Page):
    page.goto("https://www.google.com/")
    # Espera que exista el input de búsqueda
    search_box = page.get_by_role("combobox")
    expect(search_box).to_be_visible()
#haciendo pruebas sobre asserts
# Test de Playwright - validar navegación
def test_playwright_get_started(page: Page):
    page.goto("https://playwright.dev/")

    page.get_by_role("link", name="Get started").click()

    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
