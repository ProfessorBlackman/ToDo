# Generated by Django 4.1.5 on 2023-01-31 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_tasksdata_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksdata',
            name='created_at',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='tasksdata',
            name='date_completed',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='tasksdata',
            name='update_at',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
