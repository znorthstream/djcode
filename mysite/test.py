'''
команда запуска
exec(open('mysite/test.py', encoding='utf8').read())

выполнить миграцию всех баз
python manage.py migrate

валидация схемы модели
ВНИМАНИЕ приложение должно быть добавлено в INSTALLED_APPS
python manage.py check

перенести схему в БД
python manage.py makemigrations books
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
