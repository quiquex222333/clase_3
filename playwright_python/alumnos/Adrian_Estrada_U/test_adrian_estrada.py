import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://www.tigo.com.bo/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("tigo"))

def test_get_started_link(page: Page):
    page.goto("https://www.tigo.com.bo/")

    # Click the get started link.
    page.get_by_role("link", name="Contacto").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()