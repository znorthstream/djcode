'''
команда запуска
exec(open('mysite/test.py', encoding='utf8').read())

валидация схемы модели
ВНИМАНИЕ приложение должно быть добавлено в INSTALLED_APPS
python manage.py check

*****************Создание базы данных********
1)создать django представление модели модели
python manage.py makemigrations books

2)синхронизирует модели с базой данных
выполнить миграцию всех баз
python manage.py migrate
*********************************************
выведет sql из модели:
python manage.py sqlmigrate books 0001_initial

Запустить сервер
python manage.py runserver
'''

from django import template
# from django.conf import settings
# settings.configure(settings)
# t = template.Template('My name is {{ name }}.')




t = template.Template("Меня зовут {{name|length}}")
c = template.Context({'name': 'Адриан 6 тернер'})
print(t.render(c))
c = template.Context({'name': 'Фред'})
print(t.render(c))
