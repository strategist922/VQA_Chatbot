# Generated by Django 3.0.10 on 2020-10-30 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Chatbot', '0005_auto_20201030_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='QNA',
            new_name='QUESTION',
        ),
    ]
