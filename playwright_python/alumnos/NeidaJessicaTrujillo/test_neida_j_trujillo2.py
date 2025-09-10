import re
from playwright.sync_api import Page, expect
#Validar que al hacer clic en un resultado de búsqueda se abra la página de reproducción del video.
def test_youtube_reproducir_video(page: Page):
    #  Va abrir la pagina de  YouTube 1
    page.goto("https://www.youtube.com/")

    # Se va acceptar cookies si aparece el banner 2
    if page.get_by_role("button", name=re.compile("Aceptar|Accept", re.I)).is_visible():
        page.get_by_role("button", name=re.compile("Aceptar|Accept", re.I)).click()

    # Vamos a buscar una musica en especifoc 3

    search_box = page.get_by_role("combobox", name="Buscar")
    search_box.fill("Python automation tutorial")
    search_box.press("Enter")

    # Hacer clic en el primer resultado 4
    first_result = page.locator("#video-title").first
    video_title = first_result.inner_text()  # Guardar título para validación
    first_result.click()

    # Se validara  que el título del video en la página de reproducción coincida
    expect(page.locator("h1.title")).to_contain_text(re.compile(video_title[:10], re.I))  # valida usando los primeros 10 caracteres
