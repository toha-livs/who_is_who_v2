# Generated by Django 2.1 on 2018-10-05 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('who_is', '0005_auto_20181005_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='position',
            field=models.CharField(choices=[('оператор', 'OP'), ('супервайзер', 'SV'), ('тилид', 'RG'), ('другое', 'OT'), ('ОКК', 'QC')], default='оператор', max_length=15),
        ),
    ]
