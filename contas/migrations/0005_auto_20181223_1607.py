# Generated by Django 2.1.4 on 2018-12-23 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_auto_20181223_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
