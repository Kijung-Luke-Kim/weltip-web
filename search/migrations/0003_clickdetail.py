# Generated by Django 3.0.5 on 2020-06-09 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_searchobj'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentId', models.CharField(max_length=20)),
                ('contentName', models.CharField(max_length=40)),
                ('userId', models.CharField(default='anonymous', max_length=20)),
                ('userType', models.CharField(max_length=20)),
                ('cat1', models.CharField(max_length=20)),
                ('cat2', models.CharField(max_length=20)),
                ('cat3', models.CharField(max_length=20)),
            ],
        ),
    ]
