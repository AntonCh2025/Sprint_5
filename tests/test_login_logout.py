from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators as locator
from data import TestData as td


#Login пользователя
def test_login_user_exist_success(browser):

    # Нажать кнопку «Вход и регистрация».
    browser.find_element(*locator.enter_and_register_button).click()

    # Заполнить все поля формы авторизации и нажать кнопку «Войти».
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator.ent_enter_button))
    browser.find_element(*locator.ent_email_input).send_keys(td.user_exist['login'])
    browser.find_element(*locator.ent_password_input).send_keys(td.user_exist['password'])
    browser.find_element(*locator.ent_enter_button).click()

    # Проверить: произошёл переход на главную страницу, 
    #   в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator.avatar))
    avatar_is_displayed = browser.find_element(*locator.avatar).is_displayed()
    user_name_is_displayed = browser.find_element(*locator.user_name).is_displayed()
    assert avatar_is_displayed and user_name_is_displayed

#Logout пользователя
def test_logout_user_exist_success(browser):
    # Авторизоваться под заранее созданным пользователем.
    # Нажать кнопку «Вход и регистрация».
    browser.find_element(*locator.enter_and_register_button).click()

    # Заполнить все поля формы авторизации и нажать кнопку «Войти».
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator.ent_enter_button))
    browser.find_element(*locator.ent_email_input).send_keys(td.user_exist['login'])
    browser.find_element(*locator.ent_password_input).send_keys(td.user_exist['password'])
    browser.find_element(*locator.ent_enter_button).click()

    # Нажать кнопку «Выйти».
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator.exit_profile_button))
    browser.find_element(*locator.exit_profile_button).click()

    # Проверить: аватар пользователя и имя User больше не отображается в правом верхнем углу около кнопки «Разместить объявление», 
    #     там теперь отображается кнопка «Вход и регистрация».
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator.enter_and_register_button))
    avatar_not_displayed = (len(browser.find_elements(*locator.avatar)) == 0)
    user_name_not_displayed = (len(browser.find_elements(*locator.user_name)) == 0)
    enter_and_registration_button_is_displayed = browser.find_element(*locator.enter_and_register_button).is_displayed()

    assert avatar_not_displayed and user_name_not_displayed and enter_and_registration_button_is_displayed
