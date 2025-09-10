import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://demoqa.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("DEMOQA"))

def test_get_started_link(page: Page):
    page.goto("https://demoqa.com/")

    # Click the get started link.
    page.get_by_text("Book Store Application").click()

    expect(page).to_have_url("https://demoqa.com/books")

