# Generated by Django 3.2.4 on 2021-07-02 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_discussion'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='Name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
