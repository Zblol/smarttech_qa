# smarttech_qa

Для запуска теста необходимо скачать:
- интерпритатор Python (https://www.python.org/downloads/)
- Pytest (в консоли введите $ pip install -U pytest)
- ChromeDriver (https://chromedriver.chromium.org/downloads)
- ChromeDriver разместить в корневой папке с тесотом

Для запуска теста:
- открыть в терминале корневую папку
- ввести команду $  pytest  test_distance_page.py   

Для запуска теста с HTML-отчетом:
- открыть в терминале корневую папку
- ввести команду $ pytest --html=report.html --self-contained-html
