# Generated by Django 2.1 on 2018-10-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('who_is', '0003_auto_20181005_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='position',
            field=models.CharField(choices=[('OP', 'Оператор'), ('SV', 'Супервыйзер'), ('RG', 'Тимлид'), ('OT', 'Другие'), ('QC', 'OKK')], default='OP', max_length=2),
        ),
    ]