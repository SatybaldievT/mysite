# Generated by Django 5.0.dev20230410064954 on 2023-04-12 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='answ',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp.answer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='answ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.answer'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ques',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.question'),
        ),
    ]
