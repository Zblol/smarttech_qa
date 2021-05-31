from pages.base_page import BasePage
from pages.locators import YandexPageLocators


class YandexPage(BasePage):

    def go_to_target_page(self):
        search_field = self.browser.find_element(*YandexPageLocators.SEARCH_FIELD)
        search_field.send_keys('расчет расстояний между городами')
        submit_button = self.browser.find_element(*YandexPageLocators.SEARCH_BUTTON)
        submit_button.click()
        target_link = self.browser.find_element(*YandexPageLocators.TARGET_LINK)
        target_link.click()
        self.browser.switch_to.window(self.browser.window_handles[1])
