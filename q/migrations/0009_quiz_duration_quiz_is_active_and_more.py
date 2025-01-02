# Generated by Django 5.0.7 on 2024-09-20 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('q', '0008_alter_studentanswer_quiz_result_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='duration',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='quiz',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='show_results_to_student',
            field=models.BooleanField(default=True),
        ),
    ]