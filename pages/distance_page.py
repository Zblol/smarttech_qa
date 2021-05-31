from pages.base_page import BasePage
from pages.locators import DistancePageLocators


class DistancePage(BasePage):

    def text_from_to(self, city):
        from_field = self.browser.find_element(*DistancePageLocators.FROM_TO)
        from_field.send_keys(city)

    def text_where_to(self, city):
        from_field = self.browser.find_element(*DistancePageLocators.WHERE_TO)
        from_field.send_keys(city)

    def text_to_fuel_use(self, num):
        fuel_use = self.browser.find_element(*DistancePageLocators.FUEL_USE)
        fuel_use.clear()
        fuel_use.send_keys(num)

    def text_fuel_price(self, num):
        fuel_price = self.browser.find_element(*DistancePageLocators.FUEL_PRICE)
        fuel_price.clear()
        fuel_price.send_keys(num)

    def text_to_across_city(self, city):
        across_city = self.browser.find_element(*DistancePageLocators.ACROSS_CITY)
        across_city.send_keys(city)

    def button_submit_click(self):
        button = self.browser.find_element(*DistancePageLocators.COUNT)
        button.click()

    def check_distance(self, total_dist):
        distance = self.browser.find_element(*DistancePageLocators.DISTANCE).text
        assert f"{total_dist}" in distance, 'расчет дистанции некорректный'

    def check_fuel_price(self, price):
        fuel_price = self.browser.find_element(*DistancePageLocators.TOTAL_FUEL_PRICE).text
        assert f"{price}" in fuel_price, 'расчет цены за топливо не корректный'

    def setting_distance_click(self):
        setting_distance = self.browser.find_element(*DistancePageLocators.SETTING_DISTANCE)
        self.move_to_element(setting_distance)
        setting_distance.click()

    def button_submit_refresh_click(self):
        refresh_button = self.browser.find_element(*DistancePageLocators.REFRES_COUNT)
        self.move_to_element(refresh_button)
        refresh_button.click()
