# Generated by Django 4.2.1 on 2023-06-27 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sugerencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sugerencia',
            name='sugerencia',
            field=models.CharField(max_length=2200),
        ),
    ]
