# Generated by Django 2.2.24 on 2021-09-10 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=1024)),
                ('duration', models.IntegerField()),
                ('name', models.CharField(max_length=64)),
                ('url_image', models.CharField(max_length=128)),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]
