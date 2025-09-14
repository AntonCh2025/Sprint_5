from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import StartPageLocators as locator
from data import TestData as td

#Создание объявления неавторизованным пользователем
def test_create_ad_unauthorized_user_error(browser):

    # Нажать кнопку «Разместить объявление».
    browser.find_element(*locator.post_an_ad_button).click()

    # Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь».
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator.need_authorization_modal_header))
    modal_window_is_displayed = browser.find_element(*locator.need_authorization_modal).is_displayed()
    header_text_is_correct = (browser.find_element(*locator.need_authorization_modal_header).text == 'Чтобы разместить объявление, авторизуйтесь')

    assert modal_window_is_displayed and header_text_is_correct

#Создание объявления авторизованным пользователем
def test_create_ad_authorized_user_success(new_user):
    # Фикстура new_user зарегистрировала нового пользователя. В тест приходит уже залогиненная под этим пользователем страница
    # Нажать кнопку "Разместить объявление"
    WebDriverWait(new_user, 3).until(EC.visibility_of_element_located(locator.avatar))
    new_user.find_element(*locator.post_an_ad_button).click()

    # Заполнить все поля формы: «Название», «Описание товара», «Стоимость» — стоимость должна быть указана в числовом формате.
    new_good = td.new_good()

    WebDriverWait(new_user, 3).until(EC.visibility_of_element_located(locator.new_good_description))
    new_user.find_element(*locator.new_good_name).send_keys(new_good['name'])
    new_user.find_element(*locator.new_good_description).send_keys(new_good['description'])
    new_user.find_element(*locator.new_good_price).send_keys(new_good['price'])

    # Выбрать из Dropdown «Категорию» и «Город».
    new_user.find_element(*locator.new_good_category_button).click()
    new_user.find_element(By.XPATH, new_good['category_locator']).click()
    new_user.find_element(*locator.new_good_city_button).click()
    new_user.find_element(By.XPATH, new_good['city_locator']).click()

    # Выбрать RabioButton «Состояние товара».
    new_user.find_element(By.XPATH, new_good['condition_locator']).click()
    
    # Нажать кнопку «Опубликовать».
    new_user.find_element(*locator.new_good_publish_button).click()
    
    # Перейти в профиль пользователя.
    WebDriverWait(new_user, 3).until(EC.visibility_of_element_located(locator.next_page_button))
    new_user.find_element(*locator.avatar).click()

    # Проверить: в блоке «Мои объявления» отображается созданное объявление.
    WebDriverWait(new_user, 3).until(EC.visibility_of_element_located(locator.my_ad_name))
    new_ad_name = new_user.find_element(*locator.my_ad_name).text
    new_ad_city = new_user.find_element(*locator.my_ad_city).text

    assert new_ad_name == new_good['name'] and new_ad_city == new_good['city']
