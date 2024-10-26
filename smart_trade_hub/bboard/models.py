"""Модуль для хранения моделей приложения bboard.

В этом модуле определены модели, используемые в приложении для размещения 
объявлений о продаже товаров. Модуль включает в себя модель `Advertisement`, 
которая представляет собой объявление с информацией о товаре, его 
описанием, ценой и датой публикации.

Классы:
    Advertisement: Модель для представления объявлений о продаже товара.
"""

from django.db import models


class Advertisement(models.Model):
    """Модель для представления объявлений о продаже товара.
    
    Поля:
        id (PrymaryKey): поле, которое автоматически генерируется Django
        title (CharField): заголовок объявления с названием продаваемого товара
            (длина — 50 символов)
        content (TextField): сам текст объявления, описание товара, поле MEMO
        price (FloatField): цена продаваемого товара
        published (DateTimeField): дата публикации (тип — временная отметка, 
            т. е. значение даты и времени, в которые объявление было 
            опубликовано; значение по умолчанию — текущие дата 
            и время; поле индексированное)
    """

    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(verbose_name='Описание')
    price = models.FloatField()
    published = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Дата публикации'
    )

    class Meta:
        """Мета-класс для модели `Advertisement`."""

        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']

    def __str__(self) -> str:
        """Возвращает строковое представление объявления."""
        return f'{self.title}'
