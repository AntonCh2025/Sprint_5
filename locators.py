from selenium.webdriver.common.by import By


class StartPageLocators:

    # Элементы главной страницы
    enter_and_register_button = (By.XPATH, './/button[text()="Вход и регистрация"]')
    avatar = (By.XPATH, './/button[@class="circleSmall"]')
    user_name = (By.XPATH, './/h3[@class="profileText name"]')
    exit_profile_button = (By.XPATH,'.//button[text()="Выйти"]')
    post_an_ad_button = (By.XPATH, './/button[text()="Разместить объявление"]')
    need_authorization_modal = (By.XPATH, './/form[@class="popUp_shell__LuyqR"]')
    need_authorization_modal_header = (By.XPATH, './/form[@class="popUp_shell__LuyqR"]/descendant::h1')
    next_page_button = (By.XPATH, './/button[contains(@class, "right undefined")]')
    
    # Форма входа
    ent_email_input = (By.XPATH, './/input[@name="email"]')
    ent_password_input = (By.XPATH, './/input[@name="password"]')
    ent_enter_button = (By.XPATH, './/button[text()="Войти"]')
    ent_no_account_button = (By.XPATH, './/button[text()="Нет аккаунта"]')

    # Форма регистрации
    reg_email_input = (By.XPATH, './/input[@name="email"]')
    reg_password_input = (By.XPATH, './/input[@name="password"]')
    reg_confirm_password_input = (By.XPATH, './/input[@name="submitPassword"]')
    reg_create_button = (By.XPATH, './/button[text()="Создать аккаунт"]')
    reg_has_account_button = (By.XPATH, './/button[text()="Уже есть аккаунт"]')

    reg_email_input_border = (By.XPATH, './/input[@name="email"]/parent::*')
    reg_password_input_border = (By.XPATH, './/input[@name="password"]/parent::*')
    reg_confirm_password_border = (By.XPATH, './/input[@name="submitPassword"]/parent::*')
    reg_error_message = ((By.XPATH, './/span[text()="Ошибка"]'))
    
    # Страница создания объявления
    new_good_name = (By.XPATH, './/input[@name="name"]')
    new_good_description = (By.XPATH, './/textarea[@name="description"]')
    new_good_price = (By.XPATH, './/input[@name="price"]')
    new_good_category_button = (By.XPATH, './/input[@name="category"]/following-sibling::button')
    new_good_city_button = (By.XPATH, './/input[@name="city"]/following-sibling::button')
    new_good_publish_button = (By.XPATH, './/button[text()="Опубликовать"]')

    # Профиль. локаторы для опубликованного объявления
    my_ad_name = (By.XPATH, './/div[@class="about"]/h2')
    my_ad_city = ((By.XPATH, './/div[@class="about"]/h3'))
    