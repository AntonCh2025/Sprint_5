import pytest
from selenium import webdriver
from data.helpers import TestDataCreation as new
from data.data import TestDataStatic as td
from data.locators import StartPageLocators as locator


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.get(td.start_page)
    yield driver
    driver.quit()   

@pytest.fixture(scope="function")
def new_user(browser):
    # Нажать кнопку «Вход и регистрация».
    browser.find_element(*locator.enter_and_register_button).click()
    # Нажать кнопку «Нет аккаунта».
    browser.find_element(*locator.ent_no_account_button).click()

    new_user = new.new_user()
    # Заполнить поле Email формы регистрации и нажать кнопку «Создать аккаунт».
    browser.find_element(*locator.reg_email_input).send_keys(new_user['login'])
    browser.find_element(*locator.reg_password_input).send_keys(new_user['password'])
    browser.find_element(*locator.reg_confirm_password_input).send_keys(new_user['password'])
    browser.find_element(*locator.reg_create_button).click()
