# Generated by Django 4.2.4 on 2023-10-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='exam',
            field=models.CharField(max_length=20),
        ),
    ]
