import re
from playwright.sync_api import Page, expect

def test_facebook_title(page: Page):
    page.goto("https://www.facebook.com/")

    #el título contenga "Facebook"
    expect(page).to_have_title(re.compile("Facebook"))

def test_x_title(page: Page):
    page.goto("https://x.com/")

    #el título contenga "X"
    expect(page).to_have_title(re.compile("X"))


def test_youtube_title(page: Page):
    page.goto("https://www.youtube.com/")

    #el título contenga "YouTube"
    expect(page).to_have_title(re.compile("YouTube"))
