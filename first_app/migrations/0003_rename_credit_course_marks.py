# Generated by Django 4.2.5 on 2023-09-23 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_course_alter_studentmodel_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='credit',
            new_name='marks',
        ),
    ]
