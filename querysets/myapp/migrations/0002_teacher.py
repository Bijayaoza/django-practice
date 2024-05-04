# Generated by Django 4.2.7 on 2023-11-05 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('empno', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=40)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
