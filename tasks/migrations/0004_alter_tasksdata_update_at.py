# Generated by Django 4.1.5 on 2023-01-29 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_tasksdata_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksdata',
            name='update_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
