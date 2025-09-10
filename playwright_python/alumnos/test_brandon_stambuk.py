import re
from playwright.sync_api import Page, expect

def test_atb_h1_title(page: Page):
    url = "https://www.atb.com.bo/2025/09/09/historico-bolivia-vence-a-brasil-y-asegura-repechaje-al-mundial-2026/"
    page.goto(url)
    h1_locator = page.locator("h1.entry-title.penci-entry-title.penci-title-")
    expected_text = "Histórico: Bolivia vence a Brasil y asegura repechaje al Mundial 2026"
    expect(h1_locator).to_have_text(expected_text)



def test_atb_first_paragraph_contains_bolivia(page: Page):
    url = "https://www.atb.com.bo/2025/09/09/historico-bolivia-vence-a-brasil-y-asegura-repechaje-al-mundial-2026/"
    page.goto(url)
    paragraph_locator = page.locator("article p").first
    expect(paragraph_locator).to_contain_text("Bolivia")