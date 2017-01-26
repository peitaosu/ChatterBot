# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-01-22 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_chatterbot', '0006_create_conversation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='root',
            field=models.OneToOneField(help_text=b'The initiating statement in a conversation.', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='django_chatterbot.Statement'),
        ),
    ]