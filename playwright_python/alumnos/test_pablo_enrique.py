import re
from playwright.sync_api import Page, expect

# def test_prueba():
#     assert 1 == 1

# def test_prueba_2():
#     assert 1 == 0, "Error al insertar datos"

# def test_prueba_3():
#     assert 1 == 1



def test_has_title(page: Page):
    page.goto("https://google.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Google"))

def search_text(page: Page, text: str):
    page.goto("https://google.com/")
    page.get_by_role("textbox", name="Buscar").click()
    page.get_by_role("textbox", name="Buscar").fill(text)
    page.get_by_role("button", name="Buscar con Google").click()
    expect(page).to_have_title(re.compile(text))
    
def click_on_first_result(page: Page):
    page.get_by_role("link", name="Playwright: Fast and reliable end-to-end testing for modern web apps").click()
    expect(page).to_have_title(re.compile("Playwright"))