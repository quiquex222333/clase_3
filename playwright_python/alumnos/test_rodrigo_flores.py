
import pytest
from playwright.sync_api import Page

@pytest.mark.parametrize("url, expected_title", [
    ("https://www.wikipedia.org/", "Wikipedia")
])
def test_verificar_titulo_pagina(page: Page, url, expected_title):
    page.goto(url)
    title = page.title()
    #imprime el titulo de la pagina
    print(title)  
    assert title == expected_title
