# Generated by Django 5.1 on 2024-08-15 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='content',
            field=models.TextField(default='Test content'),
            preserve_default=False,
        ),
    ]
