# Generated by Django 5.0.dev20230410064954 on 2023-04-12 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_question_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='view',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
