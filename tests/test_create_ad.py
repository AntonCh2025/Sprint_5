from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.locators import StartPageLocators as locator
from data.data import TestDataStatic as td
from data.helpers import TestDataCreation as new


class TestCreateAd:

    #Создание объявления неавторизованным пользователем
    def test_create_ad_unauthorized_user_error(self, browser):

        # Нажать кнопку «Разместить объявление».
        browser.find_element(*locator.post_an_ad_button).click()

        # Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь».
        WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator.need_authorization_modal_header))
        modal_window_is_displayed = browser.find_element(*locator.need_authorization_modal).is_displayed()
        header_text_is_correct = (browser.find_element(*locator.need_authorization_modal_header).text == 'Чтобы разместить объявление, авторизуйтесь')

        assert modal_window_is_displayed and header_text_is_correct

    #Создание объявления авторизованным пользователем
    def test_create_ad_authorized_user_success(self, new_user, browser):
        # Фикстура new_user зарегистрировала нового пользователя. В тест приходит уже залогиненная под этим пользователем страница
        # Нажать кнопку "Разместить объявление"
        WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator.avatar))
        browser.find_element(*locator.post_an_ad_button).click()

        # Заполнить все поля формы: «Название», «Описание товара», «Стоимость» — стоимость должна быть указана в числовом формате.
        new_good = new.new_good()

        WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator.new_good_description))
        browser.find_element(*locator.new_good_name).send_keys(new_good['name'])
        browser.find_element(*locator.new_good_description).send_keys(new_good['description'])
        browser.find_element(*locator.new_good_price).send_keys(new_good['price'])

        # Выбрать из Dropdown «Категорию» и «Город».
        browser.find_element(*locator.new_good_category_button).click()
        browser.find_element(By.XPATH, new_good['category_locator']).click()
        browser.find_element(*locator.new_good_city_button).click()
        browser.find_element(By.XPATH, new_good['city_locator']).click()

        # Выбрать RabioButton «Состояние товара».
        browser.find_element(By.XPATH, new_good['condition_locator']).click()
        
        # Нажать кнопку «Опубликовать».
        browser.find_element(*locator.new_good_publish_button).click()
        
        # Перейти в профиль пользователя.
        WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator.next_page_button))
        browser.find_element(*locator.avatar).click()

        # Проверить: в блоке «Мои объявления» отображается созданное объявление.
        WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator.my_ad_name))
        new_ad_name = browser.find_element(*locator.my_ad_name).text
        new_ad_city = browser.find_element(*locator.my_ad_city).text

        assert new_ad_name == new_good['name'] and new_ad_city == new_good['city']
        