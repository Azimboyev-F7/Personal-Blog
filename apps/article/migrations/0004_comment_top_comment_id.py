# Generated by Django 5.2 on 2025-05-01 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='top_comment_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
