import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://www.facebook.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Facebook - Entrar o registrarse"))

def test_get_started_link(page: Page):

    page.goto("https://www.youtube.com/")

    # Esperar a que aparezca el input de búsqueda
    page.wait_for_selector("input[placeholder='Buscar']")

    # Llenar la búsqueda
    page.locator("input[placeholder='Buscar']").fill("Playwright Python")

    # Click en el botón de búsqueda
    page.locator("button[title='Buscar']").click()

    # Validar que aparezcan resultados
    expect(page.locator("ytd-video-renderer").first).to_be_visible()
