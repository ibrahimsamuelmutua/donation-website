# Generated by Django 4.2.7 on 2023-11-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(),
        ),
    ]
