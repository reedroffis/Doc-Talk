# Generated by Django 3.2.2 on 2021-05-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='address',
            field=models.TextField(default='123 Fake St', max_length=50),
            preserve_default=False,
        ),
    ]