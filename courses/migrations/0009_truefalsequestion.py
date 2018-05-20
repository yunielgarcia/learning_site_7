# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-19 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_multiplechoicequestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrueFalseQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.Question')),
            ],
            bases=('courses.question',),
        ),
    ]
