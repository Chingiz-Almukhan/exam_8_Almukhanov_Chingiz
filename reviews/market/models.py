from django.contrib.auth import get_user_model

from django.db import models

CATEGORIES = (
    ('other', 'Разное'), ('products', 'Продукты'), ('technique', 'Техника'), ('sport', 'Спорт'), ('clothes', 'Одежда'))


class Product(models.Model):
    category = models.TextField(verbose_name='Категория', choices=CATEGORIES, default='other', null=False, blank=False)
    title = models.CharField(verbose_name='Название', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Текст', max_length=3000, null=True, blank=True)
    image = models.ImageField(upload_to='product_img', default='product_img/default.png',
                              verbose_name='Изображение')

    def delete(self, using=None, keep_parents=False):
        if not self.image == 'product_img/default.png':
            self.image.delete()
        super().delete()

    # is_deleted = models.BooleanField(verbose_name='Удалено', default=False, null=False)

    def __str__(self):
        return f"{self.title} - {self.category}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Review(models.Model):
    author = models.OneToOneField(to=get_user_model(), related_name='author', on_delete=models.CASCADE,
                                  verbose_name='Автор')
    product = models.ForeignKey('market.Product', related_name='products', blank=False, verbose_name='Продукты',
                                on_delete=models.CASCADE)
    review = models.TextField(verbose_name='Отзыв', max_length=3000, null=False, blank=False)
    grade = models.IntegerField(verbose_name='Оценка', null=False, blank=False)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
