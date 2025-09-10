import re
from playwright.sync_api import Page

def test_has_title_audius(page: Page):
    # Ir a Audius Music
    page.goto("https://audius.co/")

    # Obtener el título de la página
    title = page.title()


    assert "Audius" in title, f"El título no contiene 'Audius'. Título actual: {title}"


def test_explore_link(page: Page):
    # Ir a Audius Music
    page.goto("https://audius.co/")

    # Hacer clic en el enlace "Explore"
    page.get_by_role("link", name="Explore").click()

    # Obtener texto de la cabecera
    heading = page.get_by_role("heading").inner_text()


    assert "Explore" in heading, f"No se encontró la sección Explore. Texto encontrado: {heading}"


def test_sign_in_link(page: Page):
    # Ir a Audius Music
    page.goto("https://audius.co/")

    # Hacer clic en el botón "Sign In"
    page.get_by_role("button", name="Sign In").click()

    # Verificar que aparezca el modal de inicio de sesión
    modal_text = page.inner_text("body")

    assert "Sign in to Audius" in modal_text, "No se mostró el modal de inicio de sesión"