# Generated by Django 3.1.2 on 2020-10-24 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctg', models.CharField(max_length=30)),
                ('crs', models.CharField(max_length=30)),
                ('auth', models.CharField(max_length=30)),
            ],
        ),
    ]
