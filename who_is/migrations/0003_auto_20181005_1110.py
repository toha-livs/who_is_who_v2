# Generated by Django 2.1 on 2018-10-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('who_is', '0002_auto_20181005_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='position',
            field=models.CharField(choices=[('OP', 'Оператор'), ('SV', 'Супервыйзер'), ('RG', 'Тимлид'), ('OT', 'Другие')], default='OP', max_length=2),
        ),
    ]
