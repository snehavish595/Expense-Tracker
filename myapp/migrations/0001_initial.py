# Generated by Django 4.1.4 on 2023-06-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('amount', models.IntegerField()),
                ('category', models.CharField(max_length=40)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
