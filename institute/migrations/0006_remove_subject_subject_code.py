# Generated by Django 4.0.6 on 2022-08-25 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0005_subject_subject_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='subject_code',
        ),
    ]
