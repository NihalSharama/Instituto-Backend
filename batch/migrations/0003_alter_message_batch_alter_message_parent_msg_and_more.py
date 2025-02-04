# Generated by Django 4.1 on 2022-10-13 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('batch', '0002_rename_blocklist_batch_blacklist_students_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='batch.batch'),
        ),
        migrations.AlterField(
            model_name='message',
            name='parent_msg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='batch.message'),
        ),
        migrations.AlterField(
            model_name='message',
            name='reciever',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recieved_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
