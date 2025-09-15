import datetime as dt
import random

class TestDataCreation:

    @staticmethod
    def new_user():
        some_number = round(dt.datetime.now().timestamp())
        login = f'user{some_number}@email.tst'
        password = str(some_number)
        return {'login': login, 
                'password': password}
    
    @staticmethod
    def new_good():
        cities = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Казань']
        categories = ['Авто', 'Книги', 'Садоводство', 'Хобби', 'Технологии']
        names = ['Фиговина', 'Штукенция', 'Изделие']
        goods_conditions = ['Новый', 'Б/У']

        city = random.choice(cities)
        city_locator = f'.//span[text()="{city}"]/parent::*'
        category = random.choice(categories)
        category_locator = f'.//span[text()="{category}"]/parent::*'
        name = random.choice(names) + '-' + str(round(dt.datetime.now().timestamp()))
        condition = random.choice(goods_conditions)
        condition_locator = f'.//input[@value="{condition}"]/following-sibling::div'   
        description = f'Продается {condition} {name}. Исключительно для истинных ценителей {category}'
        price = str(random.randint(1000, 9999))

        good = {
            'city': city,
            'category': category,
            'name': name,
            'price': price,
            'condition': condition,
            'description': description,
            'category_locator':category_locator,
            'city_locator': city_locator,
            'condition_locator': condition_locator
        }
        return good
