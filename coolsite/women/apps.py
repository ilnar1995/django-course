from django.apps import AppConfig


class WomenConfig(AppConfig):
    name = 'women'
    verbose_name = "Женщины мира"  # добавляем чтобы поменять название в админ панели в шапке где название проекта "WOMEN" на "ЖЕНЩИНЫ МИРА". Оно сработает только если в setting в списке INSTALLED_APPS прописать полностью название приложения.apps.WomenConfig
