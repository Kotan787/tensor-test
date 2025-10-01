
class Locator(object):

    #saby home
    contacts = '//*[contains(text(), "Контакты") and contains(@class, "sbisru-Header__menu-link")]'
    offices = '//a[contains(@href, "/contacts") and contains(@class, "sbisru-link sbis_ru-link")]'
    downloads = '//*[contains(@href,"/download")]'

    #saby contacts
    logo = '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a'
    region = '//*[contains(@class, "sbis_ru-Region-Chooser__text sbis_ru-link")]'
    partners_list = '//*[contains(@class, "sbisru-Contacts-List__item")]'
    new_region_select_link = '//*[contains(@title,"Камчатский край") and contains(@class, "sbis_ru-link")]'

    #saby downloads
    download_file = '//*[contains(@class,"sbis_ru-DownloadNew-loadLink__link js-link")]'

    #tensor home
    people_power = '//*[contains(text(), "Сила в людях")]'
    about = '//a[contains(@href, "/about") and contains(.//text(), "Подробнее") and contains(@class,"tensor_ru-link tensor_ru-Index__link")]'

    #tensor about
    images = '//*[contains(@class,"tensor_ru-About__block3-image-wrapper")]'