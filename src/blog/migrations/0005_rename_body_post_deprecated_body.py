# Generated by Django 4.1.5 on 2023-01-30 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_section_short_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='deprecated_body',
        ),
    ]
