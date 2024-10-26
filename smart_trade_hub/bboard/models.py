"""Модуль для хранения моделей приложения bboard.

В этом модуле определены модели, используемые в приложении для размещения 
объявлений о продаже товаров.

Классы:
    Advertisement: Модель для представления объявлений о продаже товара.
    Rubric: Модель для представления рубрик, к которым относятся объявления.
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
        rubric (ForeignKey): ссылка на рубрику, в которой объявление 
            размещено (поле может быть пустым)
    """

    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(verbose_name='Описание')
    price = models.FloatField()
    published = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Дата публикации'
    )
    rubric = models.ForeignKey(
        'Rubric',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Рубрика',
    )

    class Meta:
        """Мета-класс для модели `Advertisement`."""

        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']

    def __str__(self) -> str:
        """Возвращает строковое представление объявления."""
        return f'{self.title}'


class Rubric(models.Model):
    """Модель для представления рубрик объявлений.

    Поля:
        id (PrymaryKey): поле, которое автоматически генерируется Django
        name (CharField): название рубрики объявлений (длина — 20 символов)
    """

    name = models.CharField(
        max_length=20, db_index=True, verbose_name='Название рубрики'
    )

    class Meta:
        """Мета-класс для модели `Rubric`."""

        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']

    def __str__(self) -> str:
        """Возвращает строковое представление рубрики."""
        return f'{self.name}'
