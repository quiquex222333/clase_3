from playwright.sync_api import Page, expect

def test_notion_button_text(page: Page):
    # Abrir Notion
    page.goto("https://www.notion.com/es")

    button = page.get_by_text("Solicita una demo").first
    expect(button).to_have_text("Solicita una demo")
