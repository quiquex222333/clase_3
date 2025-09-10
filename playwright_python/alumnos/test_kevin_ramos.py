from playwright.sync_api import Page, expect

def test_wikipedia_language_button_text(page: Page):
    # Abrir Wikipedia
    page.goto("https://www.wikipedia.org/")

    # Buscar el botón de idioma "Español"
    button = page.get_by_text("Español").first

    # Verificar que el texto del botón sea "Español"
    expect(button).to_have_text("Español")
