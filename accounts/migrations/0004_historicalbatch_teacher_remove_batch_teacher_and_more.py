# Generated by Django 4.0.6 on 2022-08-09 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_loginotp_historicalloginotp'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalbatch',
            name='teacher',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='batch',
            name='teacher',
        ),
        migrations.AddField(
            model_name='batch',
            name='teacher',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_batches', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
