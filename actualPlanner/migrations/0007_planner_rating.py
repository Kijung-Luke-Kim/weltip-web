# Generated by Django 3.0.5 on 2020-06-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualPlanner', '0006_auto_20200603_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='planner',
            name='rating',
            field=models.BooleanField(default=False),
        ),
    ]
