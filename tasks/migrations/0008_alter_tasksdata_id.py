# Generated by Django 4.1.5 on 2023-01-31 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_tasksdata_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksdata',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
