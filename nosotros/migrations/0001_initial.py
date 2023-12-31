# Generated by Django 4.2.1 on 2023-06-04 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nosotros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='cajaderecuerdos')),
            ],
            options={
                'verbose_name': 'nosotros',
                'verbose_name_plural': 'quienessomos',
            },
        ),
    ]
