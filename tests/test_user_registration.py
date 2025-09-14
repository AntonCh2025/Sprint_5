from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators as locator
from data import TestData as td


#Регистрация пользователя
def test_user_registration_valid_email_sucess(browser):
    # Нажать кнопку «Вход и регистрация».
    browser.find_element(*locator.enter_and_register_button).click()
    
    # Нажать кнопку «Нет аккаунта».
    browser.find_element(*locator.ent_no_account_button).click()
    
    # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
    new_user = td.new_user()
    browser.find_element(*locator.reg_email_input).send_keys(new_user['login'])
    browser.find_element(*locator.reg_password_input).send_keys(new_user['password'])
    browser.find_element(*locator.reg_confirm_password_input).send_keys(new_user['password'])
    browser.find_element(*locator.reg_create_button).click()
    
    # Проверить: произошёл переход на главную страницу, 
    #         в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator.avatar))
    avatar_is_displayed = browser.find_element(*locator.avatar).is_displayed()
    user_name_is_displayed = browser.find_element(*locator.user_name).is_displayed()
    assert avatar_is_displayed and user_name_is_displayed

#Регистрация пользователя c email не по маске  *******@*******.***
def test_user_registration_invalid_email_error(browser):
    browser.find_element(*locator.enter_and_register_button).click()

    # Нажать кнопку «Нет аккаунта».
    browser.find_element(*locator.ent_no_account_button).click()

    # Заполнить поле Email формы регистрации и нажать кнопку «Создать аккаунт».
    browser.find_element(*locator.reg_email_input).send_keys(td.invalid_email_user['login'])
    browser.find_element(*locator.reg_password_input).send_keys(td.invalid_email_user['password'])
    browser.find_element(*locator.reg_confirm_password_input).send_keys(td.invalid_email_user['password'])
    browser.find_element(*locator.reg_create_button).click()

    # Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator.reg_error_message))
    email_border_color = browser.find_element(*locator.reg_email_input_border).value_of_css_property('border-bottom-color')
    email_border_is_red = (email_border_color == 'rgba(255, 105, 114, 1)')
    password_border_color = browser.find_element(*locator.reg_password_input_border).value_of_css_property('border-bottom-color')
    password_border_is_red = (password_border_color == 'rgba(255, 105, 114, 1)')
    confirm_password_color = browser.find_element(*locator.reg_confirm_password_border).value_of_css_property('border-bottom-color')
    confirm_password_is_red = (confirm_password_color == 'rgba(255, 105, 114, 1)')
    error_message_is_displayed = browser.find_element(*locator.reg_error_message).is_displayed()

    assert email_border_is_red and password_border_is_red and confirm_password_is_red and error_message_is_displayed

#Регистрация уже существующего пользователя
def test_user_registration_user_exist_error(browser):
    # Нажать кнопку «Вход и регистрация».
    browser.find_element(*locator.enter_and_register_button).click()

    # Нажать кнопку «Нет аккаунта».
    browser.find_element(*locator.ent_no_account_button).click()

    # Заполнить все поля формы регистрации данными уже существующего в системе пользователя и нажать кнопку «Создать аккаунт».
    browser.find_element(*locator.reg_email_input).send_keys(td.user_exist['login'])
    browser.find_element(*locator.reg_password_input).send_keys(td.user_exist['password'])
    browser.find_element(*locator.reg_confirm_password_input).send_keys(td.user_exist['password'])
    browser.find_element(*locator.reg_create_button).click()

    # Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator.reg_error_message))
    email_border_color = browser.find_element(*locator.reg_email_input_border).value_of_css_property('border-bottom-color')
    email_border_is_red = (email_border_color == 'rgba(255, 105, 114, 1)')
    password_border_color = browser.find_element(*locator.reg_password_input_border).value_of_css_property('border-bottom-color')
    password_border_is_red = (password_border_color == 'rgba(255, 105, 114, 1)')
    confirm_password_color = browser.find_element(*locator.reg_confirm_password_border).value_of_css_property('border-bottom-color')
    confirm_password_is_red = (confirm_password_color == 'rgba(255, 105, 114, 1)')
    error_message_is_displayed = browser.find_element(*locator.reg_error_message).is_displayed()

    assert email_border_is_red and password_border_is_red and confirm_password_is_red and error_message_is_displayed
