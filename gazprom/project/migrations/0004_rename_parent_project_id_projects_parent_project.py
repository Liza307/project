# Generated by Django 5.1 on 2024-08-16 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_rename_participant_participants_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='parent_project_id',
            new_name='parent_project',
        ),
    ]
