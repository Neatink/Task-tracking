# Generated by Django 5.1.6 on 2025-05-27 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskSystem', '0003_comment_create_date_task_deadline_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['description']},
        ),
    ]
