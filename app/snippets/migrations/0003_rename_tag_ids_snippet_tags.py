# Generated by Django 3.2.8 on 2021-10-28 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_snippet_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='tag_ids',
            new_name='tags',
        ),
    ]