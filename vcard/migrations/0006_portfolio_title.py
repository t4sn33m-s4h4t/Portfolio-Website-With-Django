# Generated by Django 4.2.1 on 2023-07-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0005_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]