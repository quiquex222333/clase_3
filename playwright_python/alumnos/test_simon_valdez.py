import re
from playwright.sync_api import Page, expect

def test_prueba():
    assert 1 == 1

def test_prueba_2():
    assert 1 == 1

def test_prueba_3():
    assert 1 == 3, "Error al insertar datos"



def test_has_title(page: Page):
    page.goto("https://es.onlinesoccermanager.com/Login")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Online"))

def test_get_started_link(page: Page):
    page.goto("https://es.onlinesoccermanager.com/Login")

    # Click the get started link.
    page.get_by_role("btn-alternative", name="Crear una cuenta").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Online")).to_be_visible()