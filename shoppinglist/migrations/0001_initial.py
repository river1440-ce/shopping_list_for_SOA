# Generated by Django 3.2.6 on 2021-08-21 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('amount', models.IntegerField(help_text='Enter what amount of this item would you like to buy.')),
                ('summary', models.TextField(help_text='Enter a brief description of the item.', max_length=1000)),
            ],
        ),
    ]
