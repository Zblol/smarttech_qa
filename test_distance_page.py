from pages.yandex_page import YandexPage
from pages.distance_page import DistancePage
import time


def test_check_fuel_price_total_distance(browser):
    link = 'https://yandex.ru/'
    browser.get(link)
    page = YandexPage(browser, link)
    page.open()
    page.go_to_target_page()
    page_distance = DistancePage
    page_distance.text_from_to(page, 'Тула')
    page_distance.text_where_to(page, 'Санкт-Петербург')
    page_distance.text_fuel_price(page, 46)
    page_distance.text_to_fuel_use(page, 9)
    page_distance.button_submit_click(page)
    page_distance.check_distance(page, 897)
    page_distance.check_fuel_price(page, 3726)
    page_distance.setting_distance_click(page)
    page_distance.text_to_across_city(page, 'Великий Новгород')
    time.sleep(30)
    page_distance.button_submit_refresh_click(page)
    page_distance.check_distance(page, 966)
    page_distance.check_fuel_price(page, 4002)


