# Generated by Django 3.0.10 on 2020-10-29 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='USER_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Chatbot.USER'),
        ),
        migrations.AlterField(
            model_name='qna',
            name='IMG_NO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Chatbot.IMAGE'),
        ),
    ]
