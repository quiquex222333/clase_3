import re

from playwright.sync_api import Page, expect

def test_validar_titulo_exacto(page: Page):
    # Abre la página toolsqa.com
    page.goto("https://www.toolsqa.com/")

    # Verificación del título exacto
    expect(page).to_have_title("Tools QA")