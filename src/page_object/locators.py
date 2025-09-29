
class Locator(object):
    contacts = '//*[contains(text(), "Контакты") and contains(@class, "sbisru-Header__menu-link")]'
    offices = '//a[contains(@href, "/contacts") and contains(@class, "sbisru-link sbis_ru-link")]'
    logo = '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a'
    people_power = '//*[contains(text(), "Сила в людях")]'
    about = '//a[contains(@href, "/about") and contains(.//text(), "Подробнее") and contains(@class,"tensor_ru-link tensor_ru-Index__link")]'
    images = '//*[contains(@class,"tensor_ru-About__block3-image-wrapper")]'