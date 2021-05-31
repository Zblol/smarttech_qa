from selenium.webdriver.common.by import By


class YandexPageLocators:
    SEARCH_FIELD = (By.ID, 'text')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'div .search2__button')
    TARGET_LINK = (By.CSS_SELECTOR, '.Link[href="https://www.avtodispetcher.ru/distance/"]')


class DistancePageLocators:
    FROM_TO = (By.CSS_SELECTOR, '[name=from]')
    WHERE_TO = (By.CSS_SELECTOR, '[name=to]')
    FUEL_USE = (By.CSS_SELECTOR, '[name=fc]')
    FUEL_PRICE = (By.CSS_SELECTOR, '[name=fp]')
    COUNT = (By.CSS_SELECTOR, '.submit_button')
    SETTING_DISTANCE = (By.CSS_SELECTOR, '#triggerFormD')
    DISTANCE = (By.CSS_SELECTOR, '#totalDistance')
    TOTAL_FUEL_PRICE = (By.CSS_SELECTOR, 'form p')
    REFRESH_COUNT = (By.CSS_SELECTOR, "form[name=CalculatorForm] .submit_button [value=Рассчитать]")
    ACROSS_CITY = (By.CSS_SELECTOR, '[name=v]')
