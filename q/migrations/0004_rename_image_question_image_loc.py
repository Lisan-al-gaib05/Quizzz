# Generated by Django 5.0.7 on 2024-08-25 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('q', '0003_question_image_delete_questionai'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='image',
            new_name='image_loc',
        ),
    ]
