# Generated by Django 3.0.3 on 2020-02-07 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_pub_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='pub_time',
        ),
    ]
