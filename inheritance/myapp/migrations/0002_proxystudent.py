# Generated by Django 4.2.7 on 2023-11-09 12:33

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyStudent',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('myapp.student',),
            managers=[
                ('Crange', django.db.models.manager.Manager()),
            ],
        ),
    ]
