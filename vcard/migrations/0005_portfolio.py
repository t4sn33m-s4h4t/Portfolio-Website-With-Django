# Generated by Django 4.2.1 on 2023-07-05 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0004_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_image', models.ImageField(upload_to='portfolio/images')),
                ('github_repo_link', models.CharField(max_length=500)),
            ],
        ),
    ]
