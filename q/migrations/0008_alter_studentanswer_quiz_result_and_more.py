# Generated by Django 5.0.7 on 2024-09-13 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('q', '0007_studentanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentanswer',
            name='quiz_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_answers', to='q.quizresult'),
        ),
        migrations.AlterField(
            model_name='studentanswer',
            name='user_answer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]