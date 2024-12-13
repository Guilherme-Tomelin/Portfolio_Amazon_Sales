import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from src.core.helpers.utilities import instantitate_logs

logger = instantitate_logs()

class NavigatorSelenium:
    def __init__(self):
        self.options = webdriver.IeOptions()
        self.options.ignore_protected_mode_settings = True
        self.driver = webdriver.Ie(options=self.options)
        

    def access_link(self, link):
        logger.info("Carregando página web...")
        self.driver.get(link)

    def click_selenium(self, locator, locator_type=None, frame=None):
        if frame:
            self.driver.switch_to.frame(frame)
        
        if locator_type:
            locator_classified = NavigatorSelenium.locator_classifier(locator_type)
        else:
            locator_classified = By.ID  

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((locator_classified, locator))
        )

        element.click()
        time.sleep(3)

    def input_text(self, locator, text, locator_type='name'):
        locator_classified = NavigatorSelenium.locator_classifier(locator_type)
        input_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((locator_classified, locator))
        )
        input_box.send_keys(text)

    def input_selection_value(self, field_name, input_name, locator_type='name'):
        locator_classified = NavigatorSelenium.locator_classifier(locator_type)
        select_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((locator_classified, input_name))
        )
        select = Select(select_element)
        select.select_by_visible_text(field_name)


    def close_browser(self):
        self.driver.quit()

    def back_page(self):
        self.driver.back()

    def get_current_html(self):
        html = self.driver.page_source
        return html

    @staticmethod
    def locator_classifier(type):
        locators = {
            'id': By.ID,
            'class': By.CLASS_NAME,
            'link_text': By.LINK_TEXT,
            'name': By.NAME,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
        }

        return locators.get(type, By.ID)  

    def accept_and_continue(self):
        WebDriverWait(self.driver, 2).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        return
