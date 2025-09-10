import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://www.twitch.tv/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Twitch"))

def test_explorar_link(page: Page):
    page.goto("https://www.twitch.tv/")

    page.get_by_role("link", name="Explorar").click()

    expect(page).to_have_url("https://www.twitch.tv/directory")
