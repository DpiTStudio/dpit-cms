# -*- coding: utf-8 -*-
import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from services.models import PricePlanFeature

for p in PricePlanFeature.objects.all():
    if 'Интеграция с CRM' in p.name:
        print(f'Found: {p.name}')
        p.name = 'Интеграция с CRM'
        p.save()
    if 'Модуль онлайн-оплаты' in p.name:
        print(f'Found: {p.name}')
        p.name = 'Модуль онлайн-оплаты'
        p.save()
