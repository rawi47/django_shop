# Generated by Django 2.1.7 on 2019-03-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='cost',
        ),
        migrations.AddField(
            model_name='article',
            name='prix',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(),
        ),
    ]
