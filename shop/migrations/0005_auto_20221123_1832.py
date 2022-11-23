# Generated by Django 3.2.15 on 2022-11-23 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20221123_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='berries',
            field=models.CharField(choices=[('0', 'нет'), ('1', 'Ежевика'), ('2', 'Малина'), ('3', 'Голубика'), ('4', 'Клубника')], default=('0', 'нет'), max_length=2, verbose_name='ягоды'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='decor',
            field=models.CharField(choices=[('0', 'нет'), ('1', 'Фисташки'), ('2', 'Безе'), ('3', 'Фундук'), ('4', 'Пекан'), ('5', 'Маршмеллоу'), ('6', 'Марципан')], default=('0', 'нет'), max_length=2, verbose_name='декор'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='form',
            field=models.CharField(choices=[('1', 'Круг'), ('2', 'Квадрат'), ('3', 'Прямоугольник')], max_length=2, verbose_name='форма'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='topping',
            field=models.CharField(choices=[('0', 'Без'), ('1', 'Белый соус'), ('2', 'Карамельный'), ('3', 'Кленовый'), ('4', 'Черничный'), ('5', 'Молочный шоколад'), ('6', 'Клубничный')], max_length=2, verbose_name='топпинг'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена заказа'),
        ),
    ]
