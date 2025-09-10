from playwright.sync_api import Page, expect

def test_titulo_obsidian(page: Page, browser):
    page = browser.new_page()
    page.goto("https://obsidian.md/") # ir a pagina
    assert page.title() == "Obsidian - Sharpen your thinking"