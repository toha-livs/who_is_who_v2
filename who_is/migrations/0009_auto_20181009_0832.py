# Generated by Django 2.1 on 2018-10-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('who_is', '0008_auto_20181009_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
