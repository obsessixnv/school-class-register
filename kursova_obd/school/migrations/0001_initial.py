# Generated by Django 4.2.6 on 2024-05-08 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='МояМодель',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_account', models.IntegerField()),
                ('login', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'account',
                'managed': False,
            },
        ),
    ]
