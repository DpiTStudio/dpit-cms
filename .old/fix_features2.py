# -*- coding: utf-8 -*-
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from services.models import PricePlanFeature

for p in PricePlanFeature.objects.all():
    print(repr(p.name))
    if 'Интеграция с CRM' in p.name:
        p.name = 'Интеграция с CRM'
        p.save()
        print('Updated CRM')
    if 'Модуль онлайн-оплаты' in p.name:
        p.name = 'Модуль онлайн-оплаты'
        p.save()
        print('Updated Oplaty')
