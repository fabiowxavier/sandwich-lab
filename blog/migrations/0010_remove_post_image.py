# Generated by Django 4.2.16 on 2024-12-04 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
