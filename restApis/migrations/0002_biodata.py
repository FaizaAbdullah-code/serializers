# Generated by Django 3.2.9 on 2022-04-03 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restApis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bioData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('rollno', models.IntegerField()),
                ('section', models.CharField(max_length=1)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
