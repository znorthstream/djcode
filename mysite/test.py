'''
команда запуска
exec(open('mysite/test.py', encoding='utf8').read())

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
