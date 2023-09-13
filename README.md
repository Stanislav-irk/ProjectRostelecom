# Итоговый проект по автоматизации тестирования QAP - 1035. Протестировать новый интерфейс авторизации в личном кабинете от заказчика Ростелеком Информационные Технологии.

→ [Требования по проекту (.doc)](https://docs.google.com/document/d/12yoTwHSTXxIUQQCH32OvlSd3QYUt_aQk/edit?usp=sharing&ouid=114302123057644378289&rtpof=true&sd=true)

→ Объект тестирования: https://b2c.passport.rt.ru

## Техническое задание:
Протестировать требования.
Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.
Провести автоматизированное тестирование продукта (не менее 20 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub.
Оформить описание обнаруженных дефектов. Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов. (если дефекты не будут обнаружены, то составить описание трех дефектов)

## Ожидаемый результат
Перечислены инструменты, которые применялись для тестирования.
Почему именно этот инструмент и эту технику.
Что им проверялось.
Что именно в нем сделано.
К выполненному заданию прикреплены:
Набор тест-кейсов.
Набор автотестов на GitHub. Обратите внимание, что в репозитории должен находиться файл README.md, где будет описано, что именно проверяют данные тестовые сценарии и какие команды необходимо выполнить для запуска тестов. Описанные команды должны работать на любом компьютере с установленными Python3 и PyTest.
Описание оформленных дефектов.

### В корне проекта содержаться:
1. conftest.py
2. README.md 
3. requirements.txt
   
### Директория pages содержит:
1. base_page.py
2. auth_page.py

### Директория tests содержит:
1. base_test.py
2. test_auth.py

### Директория utilities содержит:
1. locators.py
2. test_data.py

### Тест кейсы и баг-репорты:
https://docs.google.com/spreadsheets/d/1hvtgUnB99jjwjOEiX8X8R0yI8e9Ka1ZivB4N95Pmk4Y/edit?usp=sharing

#### При разработке тест-кейсов были применены следующие техники тест-дизайна:
1.Эквивалентное разбиение

2.Анализ граничных значений

3.Предугадывание ошибок

#### Запуск тестов:
1. Установить все библиотеки и зависимости: pip install -r requirements.txt.
2. Запустить тесты: pytest tests/test_auth.py.
