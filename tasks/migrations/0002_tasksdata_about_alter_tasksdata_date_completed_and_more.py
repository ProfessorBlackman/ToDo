# Generated by Django 4.1.5 on 2023-01-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksdata',
            name='about',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='tasksdata',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tasksdata',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
