# Playwright con Python

Como usar

crear un entorno virtual

```
python3 -m venv venv
```

moverse al entorno
```
source venv/bin/activate
```
**Nota** el directorio puede variar en Windows

instalaciones minimas
```
pip install pytest-playwright
playwright install
pytest-html
brew install allure
```
allure puede variar dependiendo al Sistema Operativo

Como ejecutar pruebas
```
pytest
pytest -v
pytest -x
pytest --html=pytest_report.html
pytest --alluredir allure-results
```