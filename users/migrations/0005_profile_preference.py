# Generated by Django 3.0.6 on 2020-05-23 10:39

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200510_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='preference',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('A0101', '자연관광지'), ('A0102', '관광자원'), ('A0201', '역사관광지'), ('A0202', '휴양관광지'), ('A0203', '체험관광지'), ('A0204', '산업관광지'), ('A0205', '건축/조형물'), ('A0206', '문화시설'), ('A0207', '축제'), ('A0208', '공연/행사')], max_length=59, null=True),
        ),
    ]
