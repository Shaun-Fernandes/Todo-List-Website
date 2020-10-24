# Generated by Django 3.1.2 on 2020-10-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='priority',
            field=models.PositiveIntegerField(choices=[(1, 'Low Priority'), (2, 'Medium Priority'), (3, 'High Priority')], default=1),
        ),
    ]