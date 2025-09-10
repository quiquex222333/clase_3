from playwright.sync_api import Page, expect

def test_youtube_logo_visible(page: Page):
    page.goto("https://www.youtube.com/")

    # Verificar que el logo de youtube sea visible
    expect(page.locator("#logo").first).to_be_visible()

def test_youtube_search_bar_visible(page: Page):
    page.goto("https://www.youtube.com/")

    # Verificar que la barra de búsqueda sea visibles
    page.locator("input[name='search_query']")


