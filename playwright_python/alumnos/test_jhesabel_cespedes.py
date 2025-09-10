import re
from playwright.sync_api import Page, expect

def test_prueba():
    assert 1 == 1

def test_prueba_2():
    assert 1 == 0, "Error al insertar datos"

def test_prueba_3():
    assert 1 == 1


def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


# 🚀 Nuevo test: Example Domain
def test_example_domain(page: Page):
    page.goto("https://example.com/")

    # Expect the title to be "Example Domain"
    expect(page).to_have_title("Example Domain")

    # Expect the page to have an <h1> with text "Example Domain"
    expect(page.get_by_role("heading", name="Example Domain")).to_be_visible()
