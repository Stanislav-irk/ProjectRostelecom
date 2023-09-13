class TestData:
    """Класс содержащий все данные для проверок авторизации."""
    incorrect_email = {
        'Stanislav-irk2@bk.ru': 'unregistered email',
        'Stanislav-irk2@bk.ro': 'invalid email',
        'sv@bk.ru': 'invalid email',
        'sa@ya.ru': 'invalid email',
        'stas@': 'invalid email',
        'stas@test': 'invalid email',
        "x" * 1: '1 symbol',
        "x" * 10: '10 symbols',
        "x" * 11: '11 symbols',
        "x" * 255: '255 symbols',
        "x" * 256: '256 symbols',
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 'russian',
        '的一是不了人我在有他这为之大来以个中上们': 'chinese',
        '|!@#$%^&*()-_=+`~?"№;:[]{}': 'specials',
        '1234567789890': 'digit'
    }

    incorrect_phone = {
        '91490710005': 'unregistered phone',
        '99999999999': 'invalid phone',
        "1" * 10: '10 symbols',
        "1" * 11: '11 symbols',
        "1" * 255: '255 symbols',
        "1" * 256: '256 symbols',
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 'russian',
        '的一是不了人我在有他这为之大来以个中上们': 'chinese',
        '|!@#$%^&*()-_=+`~?"№;:[]{}': 'specials'
    }

    incorrect_login = {
        'gate21@bk.ru': 'unregistered login',
        'sdler.': 'invalid login',
        'warning!': 'invalid login',
        "x" * 1: '1 symbol',
        "x" * 5: '5 symbols',
        "x" * 6: '6 symbols',
        "x" * 255: '255 symbols',
        "x" * 256: '256 symbols',
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 'russian',
        '的一是不了人我在有他这为之大来以个中上们': 'chinese',
        '|!@#$%^&*()-_=+`~?"№;:[]{}': 'specials',
        '12345678': 'digit'
    }

    incorrect_ls = {
        '911234567899': 'unregistered ls',
        '000000000890': 'invalid ls',
        "1" * 12: '12 symbol',
        "1" * 13: '13 symbols',
        "1" * 255: '255 symbols',
        "1" * 256: '256 symbols'
    }

    incorrect_password = {
        'Rjhkshkshd': 'unregistered password',
        "x" * 1: '1 symbol',
        "x" * 7: '7 symbols',
        "x" * 8: '8 symbols',
        "x" * 255: '255 symbols',
        "x" * 256: '256 symbols',
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 'russian',
        '的一是不了人我在有他这为之大来以个中上们': 'chinese',
        '|!@#$%^&*()-_=+`~?"№;:[]{}': 'specials',
        '12345678': 'digit'
    }

    VALID_EMAIL = "stanislav-irk@bk.ru"
    VALID_PHONE = "89149071103"
    VALID_PASSWORD = "Kontrol2023"
