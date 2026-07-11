# -*- coding: utf-8 -*-
"""Контекстный процессор для определения текущей темы сайта в зависимости от сезона."""
import datetime

def season_theme(request):
    """Возвращает название текущего сезона (spring, summer, autumn, winter) на основе месяца.
    Это значение будет доступно в шаблонах как `current_season`.
    """
    month = datetime.datetime.now().month
    if month in (12, 1, 2):
        season = "winter"
    elif month in (3, 4, 5):
        season = "spring"
    elif month in (6, 7, 8):
        season = "summer"
    else:
        season = "autumn"
    return {"current_season": season}
