# Generated by Django 4.1 on 2023-03-24 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_suggestion_author_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
